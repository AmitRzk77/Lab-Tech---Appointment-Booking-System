from django.shortcuts import render

# Create your views here.
#def branch_page(request):
#    return render(request, 'branch/branches.html')

#def branch_page(request):
#    return render(request, 'branch/branches.html', {
#        'is_admin': request.user.is_staff  # or is_superuser or a custom check
#    })
from django.shortcuts import render

def branch_page(request):
    if request.user.is_superuser:
        template_name = 'branch/branches.html'  # uses base.html
    else:
        template_name = 'branch/users_branches.html'   # uses base_user.html

    return render(request, template_name, {
        'is_admin': request.user.is_superuser  # optional if needed in template
    })

