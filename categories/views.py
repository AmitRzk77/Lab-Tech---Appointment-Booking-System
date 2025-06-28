from django.shortcuts import render

# Create your views here.
# categories/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category

def add_category_view(request):
    categories = Category.objects.filter(parent__isnull=True)  # only main categories

    if request.method == 'POST':
        category_name = request.POST.get('category')
        parent_id = request.POST.get('parent')

        parent = Category.objects.get(id=parent_id) if parent_id else None

        # Create and save new category
        Category.objects.create(category=category_name, parent=parent)
        messages.success(request, "Category Created Successfully!")
        return redirect('add_category')  # use your URL name

    return render(request, 'service/create_categories.html', {
        'categories': categories
    })
