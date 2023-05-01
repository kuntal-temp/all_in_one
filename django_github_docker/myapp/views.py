from django.shortcuts import render
from django.http import HttpResponse

def status_view(request):
    return HttpResponse("Okay")
