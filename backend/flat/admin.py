from django.contrib import admin
from .models import Flat

@admin.register(Flat)
class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')