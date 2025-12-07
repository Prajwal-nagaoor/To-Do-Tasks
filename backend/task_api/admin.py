from django.contrib import admin
from .models import taskmodel
# Register your models here.
class taskadmin(admin.ModelAdmin):
    list_display=['title','desc']
admin.site.register(taskmodel,taskadmin)