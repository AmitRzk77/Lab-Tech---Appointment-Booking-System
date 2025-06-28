from django.shortcuts import render

# Create your views here.
def contact_inquiry_list(request):
    return render(request, 'contact/contact_list.html')
