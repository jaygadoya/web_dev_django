from django.shortcuts import render
from .models import User

# Create your views here.

def homePage(request):
    user_data = User.objects.all()
    return render(request,'userLoginApp/index.html',{'users':user_data})