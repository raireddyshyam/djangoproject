from django.db import models

# Create your models here.
class Person(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(blank=True)
    JobTitle=models.CharField(max_length=30,blank=True)
    BioData=models.TextField(blank=True)