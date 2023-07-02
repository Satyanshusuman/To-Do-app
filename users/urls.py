from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path("reg/",reg),
    path("signin/",signin),
    path("signout/",signout)
    ]
