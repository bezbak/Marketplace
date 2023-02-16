from django.db import models
from apps.users.models import User
from apps.category.models import Category
# Create your models here.
class Currency(models.Model):
    name = models.CharField(
        max_length=50
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

class Product(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='product_image/'
    )
    description = models.TextField(
        max_length=500
    )
    price = models.PositiveIntegerField()
    currency = models.ForeignKey(
        Currency,
        related_name='currency',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        related_name='owner',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category_product',
    )
    PRODUCT_STATUS = (
        ('На модерации', 'На модерации'),
        ('Активный', 'Активный'),
        ('Не активный', 'Не активный'),
        ('Откланён', 'Откланён'),
    )
    product_status = models.CharField(
        choices=PRODUCT_STATUS,
        default='Активный',
        max_length=25
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
class Liked_products(models.Model):
    user = models.ForeignKey(
        User,
        related_name='liked_user',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name='liked_product',
        on_delete=models.CASCADE
    )