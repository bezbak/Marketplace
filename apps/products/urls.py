from django.urls import path
from apps.products.views import create_product
urlpatterns = [
    path('create_product/', create_product, name='create_product')
]
