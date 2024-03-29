# Daniel

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='', null=True, blank=True)
    available_quantity = models.PositiveIntegerField(default=0)




""" varianta echipa - merge
from django.db import models


class CustomProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
"""

""" bogdan
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
"""

