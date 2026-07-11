from django.db import models

# Create your models here.

class collegeStudents(models.Model):
    studentid=models.IntegerField()
    studentname=models.CharField(max_length=30)
    studentdept=models.CharField(max_length=30)