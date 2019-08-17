#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2019/3/26 16:22
# @File    : serializers.py
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
from .models import Story, Person
from rest_framework import serializers

test = 'https://www.youtube.com/results?search_query=aircraft+carrier&sp=EgIIAQ%253D%253D'


#########################
####### METHOD 1 ########
#########################
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('pid', 'pname')


class StorySerializer(serializers.ModelSerializer):
    # 相关列表中显示字符串
    # 通过调整api.models.Person.__str__来调整内容
    # person = serializers.StringRelatedField(many=True)

    # 相关列表中显示主键
    # person = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # person = serializers.PrimaryKeyRelatedField(many=True, queryset=Story.objects.all()) # 另一种写法

    # 相关列表中显示全部内容
    # 通过调整api.serializers.PersonSerializer.Meta.fields来调整内容
    person = PersonSerializer(many=True)

    class Meta:
        model = Story
        fields = ('sid', 'title', 'content', 'person')

#########################
####### METHOD 2 ########
#########################
# https://codereview.stackexchange.com/questions/164616/django-rest-framework-manytomany-relationship-through-intermediate-model
