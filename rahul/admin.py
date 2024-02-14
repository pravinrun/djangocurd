from django.contrib import admin
from .models import dhote

@admin.register(dhote)
class dhote(admin.ModelAdmin):
    list_display=['name','gmail','mobile','date']

# Register your models here.
