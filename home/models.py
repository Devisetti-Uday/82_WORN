from django.db import models
import os
from cloudinary.models import CloudinaryField

class Sell(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email=models.EmailField(null=True , blank= True)
    item = models.CharField(max_length=50)
    image = CloudinaryField('image')
    product_id = models.IntegerField(unique=True, blank=False, null=False)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} - {self.product_id} - {self.item} - ₹{self.price}"
class Order(models.Model):
    name= models.CharField( max_length=50)
    phone= models.CharField(max_length=50)
    product_id = models.IntegerField()
    def __str__(self):
        return f"{self.name} - {self.product_id}"
    