from django.urls import path
from .views import banner_text_page
from . import views
from .views import team_page
from .views import gallery_page

urlpatterns = [
    path('banner-text/', views.banner_text_page, name='banner_text'),
     path('about-us/team/', team_page, name='team-page'),
     path('about-us/gallery/', gallery_page, name='gallery-page'),
     path('about-us/popup/', views.popup_page, name='popup_page'),

]
