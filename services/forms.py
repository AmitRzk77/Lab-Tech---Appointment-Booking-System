# forms.py
from django import forms
from .models import Service, Category

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(parent__isnull=True)
        self.fields['sub_category'].queryset = Category.objects.filter(parent__isnull=False)
