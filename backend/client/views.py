from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.book_service  import BookServices


@api_view(['GET', 'POST'])
def book_list(request):
    """This API return a list of book"""
     
    if request.method == 'GET':
        data = BookServices.get_book_list()
        return Response(data)

 
