from cgi import print_exception
from ctypes import addressof
from email.mime import image
from turtle import title
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title