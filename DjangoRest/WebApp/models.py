from django.db import models

# Create your models here.
class Employees(models.Model):
    EmpId=models.IntegerField()
    FirstName=models.CharField(max_length=40)
    LastName=models.CharField(max_length=40)
    def __str__(self):
        return self.FirstName