import django
import os
from faker import Faker
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','collegeProject.settings')

django.setup()

from collegeapp.models import collegeStudents

fake=Faker()
departments = ['Aerospace','Electrical','Mechanical','Computer Science','Arts','Business Studies','MBA','Philosopy','English Literature']
def fakeData(n):
    for i in range(n):
        clg_stud = collegeStudents.objects.create(
            studentid=n,
            studentname= fake.name(),
            studentdept = fake.random.choice(departments))
        
fakeData(1000)
