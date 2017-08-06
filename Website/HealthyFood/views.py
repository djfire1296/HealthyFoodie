#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.conf import settings

from .models import *

c2s = lambda s: s.encode('UTF-8') if isinstance(s, unicode) else s 

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html', {})


def profile(request):
	name = request.user.get_username()

	userprofile = UserProfile.objects.get(name=name)
	age = userprofile.age
	country = userprofile.country
	sex = userprofile.sex
	height = userprofile.height
	weight = userprofile.weight
	disease = userprofile.disease
	physical = userprofile.physical
	tc = cal_bmr(sex, weight, height, age, physical)

	breakfast, lunch, dinner = recommend_recipe(tc, country)
	bn = breakfast.recipe_name
	bimg = breakfast.img
	ln = lunch.recipe_name
	limg = lunch.img
	dn = dinner.recipe_name
	dimg = dinner.img

	return render(request, 'profile.html', {'name': name, 'age': age, 'country': country, 'sex': sex, 'height': height, 
		'weight': weight, 'disease': disease, 'physical': physical, 'tc': tc, 'bn': bn, 'bimg': bimg, 'ln': ln,
		'limg': limg, 'dn': dn, 'dimg': dimg})

def save(request):
	return render(request, 'save.html', {})

def calc(request):
	name = request.user.get_username()

	userprofile = UserProfile.objects.get(name=name)
	rage = request.GET.get('age', '')
	rsex = request.GET.get('sex', '')
	rphysical = request.GET.get('physical', '')
	rheight = request.GET.get('height', '')
	rweight = request.GET.get('weight', '')
	rdisease = request.GET.get('disease', '')

	age = userprofile.age if rage == '' else rage
	country = userprofile.country
	sex = userprofile.sex if rsex == '' else rsex
	height = userprofile.height if rheight == '' else rheight
	weight = userprofile.weight if rweight == '' else rweight
	# disease = userprofile.disease if rdisease == '' else rdisease
	disease = "糖尿病"
	physical = userprofile.physical if rphysical == '' else rphysical

	tc = cal_bmr(sex, weight, height, age, physical)

	breakfast, lunch, dinner = recommend_recipe(tc, country, disease)
	bn = breakfast.recipe_name
	bimg = breakfast.img
	bp = breakfast.protien
	bf = breakfast.fat
	bc = breakfast.carbon
	bt = breakfast.totalcal


	ln = lunch.recipe_name
	limg = lunch.img
	lp = lunch.protien
	lf = lunch.fat
	lc = lunch.carbon
	lt = lunch.totalcal


	dn = dinner.recipe_name
	dimg = dinner.img
	dp = dinner.protien
	df = dinner.fat
	dc = dinner.carbon
	dt = dinner.totalcal

	tp = bp + lp + dp
	tf = bf + lf + df
	tc = bc + lc + dc
	tt = bt + lt + dt

	return render(request, 'calc.html', {'name': name, 'age': age, 'country': country, 'sex': sex, 'height': height, 
		'weight': weight, 'disease': disease, 'physical': physical, 'tc': tc, 'bn': bn, 'bimg': bimg, 'bp': bp, 'bf': bf,
		'bc': bc, 'bt': bt, 'ln': ln, 'limg': limg, 'lp': lp, 'lf': lf, 'lc': lc, 'lt': lt, 'dn': dn, 'dimg': dimg,
		'dp': dp, 'df': df, 'dc': dc, 'dt': dt, 'tp': tp, 'tf': tf, 'tc': tc, 'tt': tt})

def post1(request):
	return render(request, 'post_1.html', {})

def post2(request):
	return render(request, 'post_2.html', {})

def post3(request):
	return render(request, 'post_3.html', {})

def recommend_recipe(tc, country, disease=None):
	if disease is not None:
		sr = Recipe.objects.filter(disease=disease, nation=country).all()
	else:
		sr = Recipe.objects.filter(nation=country).all()

	bl = [r for r in sr if r.category == u"早餐"]
	ll = [r for r in sr if r.category == u"午餐"]

	breakfast = bl[0]
	lunch = ll[0]
	dinner = ll[1]

	return breakfast, lunch, dinner

def cal_bmr(sex, weight, height, age, physical):
	bmr = 10 * weight + 6.25 * height - 5 * age
	bmr = bmr + 5 if sex == 'M' else bmr - 161
	if physical == 'A':
		bmr = bmr * 1.2
	elif physical == 'B':
		bmr = bmr * 1.375
	elif physical == 'C':
		bmr = bmr * 1.55
	elif physical == 'D':
		bmr = bmr * 1.725
	else:
		bmr = bmr * 1.9
	return bmr
