from django.urls import path
from . import views

urlpatterns = [
    path('creation/', views.create_post, name='creation'),
]