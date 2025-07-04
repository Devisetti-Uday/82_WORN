from django.db import models
import uuid
import os

def unique_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('product_images/', filename)

class Sell(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to=unique_image_path)
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
    