from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.products_services import ProductServices
from services.portfolio_services import PortfolioServices
from services.book_service  import BookServices
from services.team_services import TeamServices
from services.about_services import AboutServices



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

@api_view(['GET', 'POST'])
def portfolio_list(request):
    """This API return a portfolio"""
    if request.method == 'GET':
        data = PortfolioServices.get_portfolio_list()
        return Response(data)


@api_view(['GET', 'POST'])
def team(request):
    """This API return a list of team members"""
    if request.method == 'GET':
        data = TeamServices.get_team_list()
        return Response(data)

@api_view(['GET', 'POST'])
def about(request):
    """This API return a services """
    if request.method == 'GET':
        data = AboutServices.get_about_list()
        return Response(data)