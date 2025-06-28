from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

#@login_required
def socialmedia_page(request):
    if request.user.is_superuser:
        template_name = 'socialmedia/socialmedia_list.html'
    else:
        template_name = 'socialmedia/users_socialmedia.html'

    return render(request, template_name, {
        'is_admin': request.user.is_superuser,
    })
