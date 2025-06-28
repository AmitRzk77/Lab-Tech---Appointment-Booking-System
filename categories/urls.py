# categories/urls.py
from django.urls import path
from .views import add_category_view

urlpatterns = [
    path('add/', add_category_view, name='add_category'),
]
