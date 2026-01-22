from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colecao/', views.collection, name='collection'),
    path('contato/', views.contact, name='contact'),
]
