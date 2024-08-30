from django.db import models
from Accounts.models import User

# Create your models here.

class Style(models.Model):
    style_name = models.CharField(max_length=50, unique=True)
    preview = models.ImageField(upload_to='styles/previews/', blank=True, null=True)

    def __str__(self):
        return self.style_name
    
class Type(models.Model):
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type_name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/images/', blank=False)
    image_thumbnail = models.ImageField(upload_to='posts/thumbnails/', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='posts')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title