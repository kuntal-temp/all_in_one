from django.urls import path
from .views import *


urlpatterns = [
    path('', health_check_view, name="health_check_url"),
]
