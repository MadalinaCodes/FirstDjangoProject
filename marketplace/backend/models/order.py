# Daniel

from django.db import models

from .product import Product
from .user import CustomUser

class Order(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # CASCADE FACE CA TOT CE TINE DE UN ANUMIT USER SA SE STEARGA ODATA CU USERUL
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)




















""" varianta echipa - merge
from django.db import models

from .product import CustomProduct


class CustomOrder(models.Model):
    products = models.ManyToManyField(CustomProduct)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.created_at}"
"""

""" bogdan
    class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    products = models.ManyToManyField(Product)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    creat
"""

