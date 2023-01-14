from django.contrib import admin
from.models import *

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['name','department','course']

admin.site.register(userData,userAdmin)