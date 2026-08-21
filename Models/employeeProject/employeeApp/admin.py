from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'emp_name', 'emp_address', 'emp_phonenumber', 'emp_title']



admin.site.register(Employee,EmployeeAdmin)