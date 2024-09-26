from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    role=models.CharField(max_length=100)
    salary=models.IntegerField()