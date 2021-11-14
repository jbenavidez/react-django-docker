from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.products_services import ProductServices
from services.book_service  import BookServices
 

@api_view(['GET', 'POST'])
def book_list(request):
    """This API return a list of book"""
    if request.method == 'GET':
        data = BookServices.get_book_list()
        return Response(data)

 
@api_view(['GET', 'POST'])
def services_list(request):
    """This API return a list of services"""
    if request.method == 'GET':
        data = ProductServices.get_product_services()
        return Response(data)

 