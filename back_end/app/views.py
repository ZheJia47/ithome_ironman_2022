from django.shortcuts import render
from django.http import JsonResponse, response
from django.conf import settings

# Create your views here.

def function1(request):
    # get paramater from front-end
    param1=request.GET['param1']
    # response data to front-end
    response={}
    response['msg']='hello world'
    return JsonResponse(response)