from django.db import models

# Create your models here.

class Emp(models.Model):
    Eid = models.IntegerField()
    Name = models.CharField(max_length=200)
    Sala = models.IntegerField()
    Loca = models.CharField(max_length=100)
    Posi = models.CharField(max_length=100)