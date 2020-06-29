from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.FloatField()
    original_price = models.FloatField()
    productTypes = ( ('D','Desktops'),
                     ('L','Laptops'),
                     ('P','Printers'),
                     ('O','Peripherals'),
                     ('A','Apple Products'),
                     ('C','CCTV Cameras'))
    productType = models.CharField(max_length=1, choices=productTypes) 
    image = models.ImageField(upload_to="products",null = True,blank = True)
