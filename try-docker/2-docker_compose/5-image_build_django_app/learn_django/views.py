from django.shortcuts import render
from django.http import HttpResponse


def health_check_view(request):
    return HttpResponse("Health is Ok ✅")
