from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from faqs.models import FAQ
from django.contrib import messages

def faq_page(request):
    faqs = FAQ.objects.all().order_by('-id')

    if request.user.is_superuser:
        template_name = 'FAQs/faqs.html'
    else:
        template_name = 'FAQs/users_faqs.html'

    return render(request, template_name, {
        'faqs': faqs,
        'is_admin': request.user.is_superuser
    })


def add_faq(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        FAQ.objects.create(title=title, description=description)
        messages.success(request, "FAQ added successfully!")
    return redirect('faq_page')

def edit_faq(request, id):
    faq = get_object_or_404(FAQ, id=id)
    if request.method == 'POST':
        faq.title = request.POST.get('title')
        faq.description = request.POST.get('description')
        faq.save()
        messages.success(request, "FAQ updated successfully!")
    return redirect('faq_page')

def delete_faq(request, id):
    faq = get_object_or_404(FAQ, id=id)
    faq.delete()
    messages.success(request, "FAQ deleted successfully!")
    return redirect('faq_page')
