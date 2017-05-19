from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField()
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.Foreignkey(Manufacturer)

class Manufacturer(models.Model):
    name = models.CahrField(max_length=255)