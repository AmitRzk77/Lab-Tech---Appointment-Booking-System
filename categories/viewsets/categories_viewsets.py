from rest_framework import viewsets
from ..serializers.categories_serializers import CategorySerializer, SubCategorySerializer
from ..models import Category
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    #permission_classes= [IsAdminUser,]
    queryset = Category.objects.filter(parent__isnull=True).order_by('-id')
    
    filter_backends = (SearchFilter,)
    search_fields = ['category']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    

    