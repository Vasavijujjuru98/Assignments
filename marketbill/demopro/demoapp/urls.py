from django.urls import path
from .views import AddProductView, CustomerPurchaseView
 
urlpatterns = [
    path('addproducts/', AddProductView.as_view(), name='add_product_api'),
    path('api/customers/purchase/<int:customer_id>/', CustomerPurchaseView.as_view(), name='customer_purchase_api'),
]