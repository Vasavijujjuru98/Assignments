
from decimal import Decimal
from django.shortcuts import render
# billing/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer
 
# First API: Add products to the Product table
class AddProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class CustomerPurchaseView(APIView):
    def post(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
 
        total_products = 0
        total_amount = Decimal('0.00')  # Initialize as Decimal
 
        for item in request.data.get("products", []):
            try:
                product = Product.objects.get(id=item["product_id"])
            except Product.DoesNotExist:
                return Response({"error": f"Product ID {item['product_id']} not found"}, status=status.HTTP_404_NOT_FOUND)
 
            quantity = item.get("quantity", 1)
            if product.stock < quantity:
                return Response({"error": f"Not enough stock for product {product.name}"}, status=status.HTTP_400_BAD_REQUEST)
 
            total_products += quantity
            total_amount += product.price * Decimal(quantity)  # Ensure both are Decimals
 
            # Reduce stock
            product.stock -= quantity
            product.save()
 
        # Update customer record
        customer.total_products = total_products
        customer.total_amount = total_amount
        customer.save()
 
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)