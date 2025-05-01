from rest_framework import viewsets
from ..serializers.faqs_serializers import FAQsSerializers
from ..models import FAQ
#from ..utilities.pagination import MyPagenumberPagination
#from rest_framework.permissions import IsAuthenticated


class faqsViewsets(viewsets.ModelViewSet):
    serializer_class = FAQsSerializers
    queryset = FAQ.objects.all().order_by('-id')