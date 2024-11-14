# billing/serializers.py
from rest_framework import serializers
from .models import Product, Customer

class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(required=False)  # Make stock optional

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'total_products', 'total_amount']
