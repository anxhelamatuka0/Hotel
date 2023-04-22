from django.contrib import admin

# Register your models here.

from .models import Feature, Room
admin.site.register(Feature)
admin.site.register(Room)