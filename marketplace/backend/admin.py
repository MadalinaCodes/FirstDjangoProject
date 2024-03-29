from django.contrib import admin

from .models.order import Order
from .models.product import Product
from .models.user import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)