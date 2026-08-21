from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=500)
    emp_phonenumber=models.IntegerField()
    emp_title = models.CharField(max_length=100)
