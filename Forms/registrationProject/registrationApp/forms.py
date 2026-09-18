from django import forms

class registration(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)


    def clean_name(self):
        if len(self.cleaned_data["name"]) <= 2:
            raise forms.ValidationError("The name field shall contain more than 2 characters...")
        return self.cleaned_data["name"]