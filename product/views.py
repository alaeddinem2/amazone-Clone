from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import Product,Review,ProductImage,Brand

# Create your views here.

class ProductList(ListView):
    model = Product
    
    

class ProductDetail(DetailView):
    model = Product
