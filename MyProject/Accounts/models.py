from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    job = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='users/avatars/', blank=False)
    avatar_thumbnail = models.ImageField(upload_to='users/thumbnails/', blank=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username
    