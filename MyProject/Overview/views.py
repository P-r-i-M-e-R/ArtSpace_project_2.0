from django.shortcuts import render
from .models import Category, Post
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

# API для получения категорий
def get_categories(request):
    categories = Category.objects.all()
    data = [{'id': cat.id, 'name': cat.name, 'preview': cat.preview.url if cat.preview else None} for cat in categories]
    return JsonResponse(data, safe=False)

# API для получения постов
def get_posts(request):
    posts = Post.objects.all()
    data = [{
        'title': post.title,
        'image': post.image.url,
        'author_name': post.author_name,
        'category': post.category.name
    } for post in posts]
    return JsonResponse(data, safe=False)
