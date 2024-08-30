from django import forms
from .models import Post

class Post_Creation_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'style', 'type', 'category']
