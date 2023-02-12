from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.validators import validate_file_extension
# Create your models here.

class User(AbstractUser):
    profile_image = models.FileField(
        upload_to='profile_image/',
        validators=[validate_file_extension]
    )
    email = models.EmailField()
    about_self = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'