

from django.urls import path, include
from products_app.api.views import ProductsList, ProductDetail, GroupedProducts

urlpatterns = [
    
    path('list/', ProductsList.as_view(), name='products-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-details'),
    path('grouped-products/', GroupedProducts.as_view(), name='grouped-products-detail'),
]
