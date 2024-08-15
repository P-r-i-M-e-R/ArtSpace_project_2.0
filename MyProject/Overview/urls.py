from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/posts/', views.get_posts, name='get_posts'),
]