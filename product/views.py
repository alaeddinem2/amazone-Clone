from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import Product,Review,ProductImage,Brand

# Create your views here.

class ProductList(ListView):
    model = Product
    
    

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] =Review.objects.filter(Product=self.get_object())
        context["retaled_products"]=Product.objects.filter(brand=self.get_object().brand)
        return context
    

class BrandList(ListView):
    model = Brand

class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    
    
       
    
