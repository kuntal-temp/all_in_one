from django.urls import path
from .views import *

urlpatterns = [

    path('', status_view, name="status_check"),
]