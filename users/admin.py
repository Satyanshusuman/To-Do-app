from django.contrib import admin
from .models import *

@admin.register(Tasks)
class Customeradmin(admin.ModelAdmin):
    list_display=["id","user","title"]
