#############################
##### class-based view ######
#############################

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

from api.models import Story, Person
from api.serializers import StorySerializer, PersonSerializer

from rest_framework import generics
#
#
# ListCreateAPIView
# class StoryList(generics.ListAPIView):
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer

# def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)


# RetrieveUpdateDestroyAPIView
# class StoryDetail(generics.RetrieveAPIView):
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer
#
#
# class PersonList(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#
# class PersonDetail(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


#############################
#### function based view ####
#############################

from rest_framework.decorators import api_view
from api.models import Person, Story
from api.serializers import StorySerializer, PersonSerializer
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET', 'POST'])
@api_view(['GET'])
def story_list(request):
    """
    List all code stories, or create a new story.
    :param request:
    :return:
    """
    if request.method == 'GET':
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = StorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def story_detail(request, pk):
    """
    Retrieve, update or delete a story.
    """
    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StorySerializer(story)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = StorySerializer(story, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # elif request.method == 'DELETE':
    #     story.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
