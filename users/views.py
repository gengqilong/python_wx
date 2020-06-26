import json

from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django.views import View

def register(request):
    data={}
    if request.method=="GET":
        a = request.GET.get('a', '')
        data['a']=a
    return HttpResponse(json.dumps(data))

