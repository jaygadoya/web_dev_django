from django.shortcuts import render
from collegeapp.models import *
# Create your views here.

def home(request):
    colStud = collegeStudents.objects.order_by('id')
    return render(request,'collegeapp/index.html',{'colStud':colStud})