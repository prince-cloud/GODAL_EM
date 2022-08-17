from urllib.request import Request
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Meter)
admin.site.register(Request)