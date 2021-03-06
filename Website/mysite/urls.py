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

from django.conf.urls import include, url
from django.contrib import admin

from views import *
from HealthyFood.views import *

urlpatterns = [
    url(r'^$', init_index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', loginpage),
    url(r'^account/login/$', login),
    url(r'^profile/$', profile),
    url(r'^index', index),
   	url(r'^save', save),
   	url(r'^calc/$', calc),
   	url(r'^post1', post1),
   	url(r'^post2', post2),
   	url(r'^post3', post3),
]
