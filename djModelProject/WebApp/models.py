from django.db import models

# Create your models here.

class Emp(models.Model):
    EmpID = models.IntegerField()
    EmpName = models.CharField(max_length=100)
    EmpSal = models.IntegerField()
    EmpAdd = models.CharField(max_length=100)


