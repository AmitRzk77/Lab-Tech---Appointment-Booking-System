from django.urls import path
from . import views

urlpatterns = [
    path('socialmedia/', views.socialmedia_page, name='socialmedia_page'),
]
