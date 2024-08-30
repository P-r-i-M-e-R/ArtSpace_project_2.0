from django.shortcuts import render
from Posts.models import Style, Type, Post
from django.http import JsonResponse

# Create your views here.

def overview(request):
    return render(request, 'overview.html')

# API для получения стилей
def get_styles(request):
    styles = Style.objects.all()
    data = [{'id': style.id, 'style_name': style.style_name, 'preview': style.preview.url if style.preview else None} for style in styles]
    return JsonResponse(data, safe=False)

# API для получения типов
def get_types(request):
    types = Type.objects.all()
    data = [{'id': type.id, 'type_name': type.type_name} for type in types]
    return JsonResponse(data, safe=False)

# API для получения постов страницы overview
def get_posts(request):
    posts = Post.objects.all()
    data = [{
        'title': post.title,
        'image_thumbnail': post.image_thumbnail.url,
        'author': post.author.username,
        'job': post.author.job,
        'style': post.style.style_name,
        'type': post.type.type_name,
        'category': post.category
    } for post in posts]
    return JsonResponse(data, safe=False)
