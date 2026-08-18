from django.db import models

class Department(models.TextChoices):
    IT = "IT", "IT"
    DATA_SOLUTIONS = "DATA_SOLUTIONS", "Data Solutions"
    ERP = "ERP", "ERP"
    TESTING = "TESTING", "Testing"
    SOFTWARE_DEV = "SOFTWARE_DEV", "Software Development"

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    dept = models.CharField(
        max_length=50,
        choices=Department.choices,
        default=Department.IT
    )

    def __str__(self):
        return f"{self.user_name} ({self.dept})"