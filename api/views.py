from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, ming!")


def test(request):
    d1 = {'sid': 1, 'title': 'my test title'}
    result = json.dumps(d1)
    return HttpResponse(result)


def
