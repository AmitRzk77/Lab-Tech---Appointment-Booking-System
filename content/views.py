from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Banner

def banner_text_page(request):
    banner = Banner.objects.first()  # Only one active banner
    return render(request, 'contents/banner_list.html', {'banner': banner})



def team_page(request):
    if request.user.is_superuser:
        template_name = 'contents/team_list.html'  # Extends base.html
    else:
        template_name = 'contents/users_teams.html'   # Extends base_user.html

    
    
    return render(request, template_name, {
        'is_admin': request.user.is_superuser  # Optional for template logic
    })


def gallery_page(request):
    if request.user.is_superuser:
        template_name = 'contents/gallery.html'
    else:
        template_name = 'contents/user_gallery.html'

    return render(request, template_name, {
        'is_admin': request.user.is_superuser
    })

def popup_page(request):
    return render(request, 'contents/popup_list.html')
