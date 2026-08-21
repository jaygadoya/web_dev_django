import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','employeeProject.settings')
django.setup()
from employeeApp.models import Employee
import faker

faker = faker.Faker()



for i in range(1,1001):
    number = i
    name = faker.name()
    address = faker.address()
    phone_num = random.randint(9000000000,9999999999)
    title = random.choice(['IT','Software Engineer','Data Engineer','Data Analyst','Business Analyst','SRE','SDE-1'])
    emp_records = Employee.objects.get_or_create(emp_no=number,emp_name=name,emp_address=address,emp_phonenumber=phone_num,emp_title=title)

