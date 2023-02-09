from django.urls import path
from apps.products.views import create_product, product_detail, product_update, product_delete
urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('product_update/<int:id>/', product_update, name='product_update'),
    path('product_delete/<int:id>/', product_delete, name='product_delete'),
]
