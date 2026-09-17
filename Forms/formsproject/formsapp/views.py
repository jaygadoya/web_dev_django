from django.shortcuts import render
from . import forms
# Create your views here.

def homePage(request):
    form = forms.studentRegistration()
    return render(request,'formsapp/register.html',{'formData':form})

