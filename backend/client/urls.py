from django.urls import path

from . import views

urlpatterns = [
    path('book/', views.book_list, name='book_list'),
    path('services/', views.services_list, name='services_list'),
    path('portfolio/', views.portfolio_list, name='services_list'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
]


