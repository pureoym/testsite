#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2019/3/13 11:28
# @File    : urls.py
# Copyright 2017 pureoym. All Rights Reserved.
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
# ========================================================================
from django.urls import path
from api import views

#############################
#### function based view ####
#############################
urlpatterns = [
    path('story/', views.story_list),
    path('story/<int:pk>/', views.story_detail),
]


#############################
##### class-based view ######
#############################
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = [
#     path('story/', views.StoryList.as_view()),
#     path('story/<int:pk>/', views.StoryDetail.as_view()),
#     path('person/', views.PersonList.as_view()),
#     path('person/<int:pk>/', views.PersonDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
