from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq_page, name='faq_page'),
    path('faq/add/', views.add_faq, name='add_faq'),
    path('faq/edit/<int:id>/', views.edit_faq, name='edit_faq'),
    path('faq/delete/<int:id>/', views.delete_faq, name='delete_faq'),
]
