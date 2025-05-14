from django.shortcuts import render
from categories.models import Category

# Create your views here.


def service_page(request):
    return render(request, 'service/service.html')

def manage_groups_view(request):
    return render(request, 'service/manage_groups.html')  # Adjust path if needed

from django.shortcuts import render, redirect
from .forms import ServiceForm  # Make sure this form is defined

from django.shortcuts import render, redirect
from services.models import Category, Service  # adjust as per your model
from django.views.decorators.csrf import csrf_exempt
from django import forms

def add_service(request):
    categories = Category.objects.filter(parent__isnull=True)
    subcategories = Category.objects.filter(parent__isnull=False)

    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        category_id = request.POST.get('category')  # Category ID selected in form
        subcategory_id = request.POST.get('subcategory')  # Subcategory ID selected in form
        price = request.POST.get('price')
        tags = request.POST.get('tags')
        description = request.POST.get('description')
        featured_img = request.FILES.get('featured_img')  # Correct field for feature image
        other_img = request.FILES.get('other_img')  # Correct field for other image

        # Get the category and subcategory objects using their IDs
        category = Category.objects.get(id=category_id)  # Fetch the category object
        subcategory = Category.objects.get(id=subcategory_id) if subcategory_id else None  # Fetch subcategory if provided

        # Create the service object and save it to the database
        service = Service.objects.create(
            name=name,
            category=category,  # Pass the category object
            sub_category=subcategory,  # Pass the subcategory object
            price=price,
            tags=tags,
            description=description,
            featured_img=featured_img,  # Save the feature image
            other_img=other_img  # Save the other image
        )

        # Redirect to the same page or a success page
        return redirect('add_service')  # Replace with the correct URL name for your view

    # If GET request, show form with categories and subcategories
    form = ServiceForm()  # Initialize the form (assuming you have one for service)
    return render(request, 'service/add_services.html', {
        'categories': categories,
        'subcategories': subcategories,
        'form': form  # Pass form to context if you want to render it in the template
    })