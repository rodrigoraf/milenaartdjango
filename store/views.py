from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'store/home.html')

def collection(request):
    products = Product.objects.all()
    return render(request, 'store/collection.html', {'products': products})

def contact(request):
    return render(request, 'store/contact.html')
