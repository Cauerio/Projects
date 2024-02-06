from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)
