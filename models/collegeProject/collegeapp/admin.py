from django.contrib import admin
from collegeapp.models import *
# Register your models here.

class collegeStudentsAdmin(admin.ModelAdmin):
    list_display = ['studentid', 'studentname', 'studentdept']

admin.site.register(collegeStudents,collegeStudentsAdmin)
