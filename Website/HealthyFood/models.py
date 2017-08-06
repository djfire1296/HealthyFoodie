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

from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    cook = models.CharField(max_length=5)
    ingredient = models.CharField(max_length=500)
    img = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    note = models.CharField(max_length=500)
    protien = models.FloatField()
    fat = models.FloatField()
    carbon = models.FloatField()
    totalcal = models.FloatField()
    nation = models.CharField(max_length=50)


class UserProfile(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	country = models.CharField(max_length=20)
	sex = models.CharField(max_length=5)
	height = models.FloatField()
	weight = models.FloatField()
	disease = models.CharField(max_length=20)
	physical = models.CharField(max_length=50)

class NutritionClinic(models.Model):
	name = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	num = models.IntegerField()

	