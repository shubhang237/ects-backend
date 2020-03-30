from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="products/images/",null = True,blank = True)
