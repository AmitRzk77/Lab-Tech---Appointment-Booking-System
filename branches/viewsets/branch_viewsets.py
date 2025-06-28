from rest_framework import viewsets
from ..serializers.branches_serializers import BranchListSerializers,BranchRetriveSerializers,BranchWriteSerializers
from ..models import Branch

#from ..utilities.pagination import MyPagenumberPagination
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import IsAuthenticatedOrReadOnly


class branchesViewsets(viewsets.ModelViewSet):
    serializer_class = BranchListSerializers
    queryset = Branch.objects.all().order_by('-id')
    #pagination_class = MyPagenumberPagination
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]


def get_queryset(self):
    queryset = super().get_queryset()  #here we can apply authorization for data
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return BranchWriteSerializers
    elif self.action == 'retrieve':
        return BranchRetriveSerializers
    return super().get_serializer_class()
