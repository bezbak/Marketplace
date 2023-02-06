from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'