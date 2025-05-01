from rest_framework import viewsets, filters
from ..serializers.categories_serializers import CategorySerializer
#from ..utilities.pagination import MyPagenumberPagination
#from rest_framework.permissions import IsAuthenticated
from ..models import Category
from django_filters.rest_framework import DjangoFilterBackend



class categoriesViewsets(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent__isnull=True).order_by('-id')
    
    #pagination_class = MyPagenumberPagination
   # permission_classes = [IsAuthenticated]


def get_queryset(self):
    queryset = super().get_queryset()  #here we can apply authorization for data
    return queryset


