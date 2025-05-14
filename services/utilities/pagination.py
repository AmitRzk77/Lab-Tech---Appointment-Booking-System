from rest_framework.pagination import PageNumberPagination

class MyPagenumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'param'
    page_size_query_param = 'size'
    max_page_size = 5000