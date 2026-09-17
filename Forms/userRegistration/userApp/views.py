from django.shortcuts import render
from . import forms
# Create your views here.


def homePage(request):
    formTemplate = forms.userRegister()
    if request.method == "POST":
        submittedForm = forms.userRegister(request.POST)
        if submittedForm.is_valid():
            print("Validation Completed...")
            print(f"Name of the person is: {submittedForm.cleaned_data["name"]}")
            print(f"Age is: {submittedForm.cleaned_data["age"]}")
            print(f"Email ID is: {submittedForm.cleaned_data["email"]}")
            print(f"feedback provided is: {submittedForm.cleaned_data["feedback"]}")
            print("End of form...")


    return render(request,'userApp/register.html',{'formData':formTemplate})