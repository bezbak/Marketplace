from django.db import models
from apps.users.models import User
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
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'