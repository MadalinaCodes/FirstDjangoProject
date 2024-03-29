
from rest_framework import serializers
from .models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'available_quantity')
