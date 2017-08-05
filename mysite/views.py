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

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.conf import settings
from django.contrib import auth

import logging

# from .models import *

def init_index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html', {})
    # return HttpResponseRedirect('/')

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'index.html', {})
    return HttpResponseRedirect('/')

def loginpage(request):
	# return HttpResponseRedirect('login.html')
	return render(request, 'login.html', {})


def login(request):
	if request.user.is_authenticated():
		# return render(request, 'profile.html', {})
		return HttpResponseRedirect('/profile/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		# return render(request, 'profile.html', {})
		return HttpResponseRedirect('/profile/')
	else:
		return render(request, 'login.html', locals())

def profile(request):
	return render(request, 'profile.html', {})

def save(request):
	return render(request, 'save.html', {})

def calc(request):
	return render(request, 'calc.html', {})

