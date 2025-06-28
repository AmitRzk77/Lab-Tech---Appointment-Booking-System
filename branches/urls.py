from django.urls import path
from .views import branch_page
from . import views

urlpatterns = [
    path('branches/', views.branch_page, name='branch_page'),
]
