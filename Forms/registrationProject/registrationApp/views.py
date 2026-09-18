from django.shortcuts import render
from . import forms
# Create your views here.

def registerPage(request):
    displayForm = forms.registration()

    if request.method == "POST":
        submittedForm = forms.registration(request.POST)
        if submittedForm.is_valid():
            print(f"The name is: {submittedForm.cleaned_data["name"]}")
            print(f"The email id is: {submittedForm.cleaned_data["email"]}")
            print(f"The age of the user is: {submittedForm.cleaned_data["age"]}")
            print(f"The feedback provided by the user is: {submittedForm.cleaned_data["feedback"]}")

        displayForm = submittedForm

    return render(request,'registrationApp/registration.html',{'items':displayForm})
