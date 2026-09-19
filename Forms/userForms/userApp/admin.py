from django.contrib import admin
from .models import student

class studentAdmin(admin.ModelAdmin):
    list_display = ['name','age']
# Register your models here.
admin.site.register(student,studentAdmin)

