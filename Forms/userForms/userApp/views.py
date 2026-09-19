from django.shortcuts import render
from . import forms
# Create your views here.
def formRegistration(request):
    form = forms.registration
    if request.method == "POST":
        form = forms.registration(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data is successfully stored in Database...")

    return render(request,'userApp/registration.html',{'form':form})
