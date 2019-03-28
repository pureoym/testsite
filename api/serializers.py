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

test='https://www.youtube.com/results?search_query=aircraft+carrier&sp=EgIIAQ%253D%253D'


# class StorySerializer(serializers.Serializer):
#     sid = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Story` instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return Story.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Story` instance, given the validated data.
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.save()
#         return instance

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('sid','title','content')