from django.db import models

# Create your models here.
class Mobile(models.Model):
    name=models.CharField(max_length=100)
    modal=models.CharField(max_length=100)
    company_price=models.IntegerField()
    max_price=models.IntegerField()

    
