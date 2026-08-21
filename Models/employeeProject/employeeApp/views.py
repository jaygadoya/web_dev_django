from django.shortcuts import render
from .models import Employee
# Create your views here.

def homePage(request):
    # employee = Employee.objects.all()
    return render(request,'employeeApp/index.html')

def shiftPage(request):
    employee = Employee.objects.all()
    return render(request,'employeeApp/display.html',{'employees':employee})
