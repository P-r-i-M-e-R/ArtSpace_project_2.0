from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('api/styles/', views.get_styles, name='get_styles'),
    path('api/types/', views.get_types, name='get_types'),
    path('api/posts/', views.get_posts, name='get_posts'),
]