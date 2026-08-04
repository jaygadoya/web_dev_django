from django.shortcuts import render
from datetime import datetime
# Create your views here.
def homePage(request):
    now = datetime.now()
    dict = {'x':now}

    return render(request,'tempTagsApp/index.html',context=dict)