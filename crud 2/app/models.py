from django.db import models

# Create your models here.
class Car(models.Model):
    brand  =  models.CharField(max_length=100)
    modal  =  models.CharField(max_length=100)
    showroom_price  =  models.CharField(max_length=100)
    on_road_price  =  models.CharField(max_length=100)