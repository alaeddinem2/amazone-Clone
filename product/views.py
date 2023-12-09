from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import Product,Review,ProductImage,Brand
from django.db.models import Q , F
from django.db.models.aggregates import Max, Min, Avg, Count, Sum

# Create your views here.
class ProductList(ListView):
    model = Product
    paginate_by = 24
    
    

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] =Review.objects.filter(Product=self.get_object())
        context["retaled_products"]=Product.objects.filter(brand=self.get_object().brand)
        return context
    

class BrandList(ListView):
    model = Brand
    paginate_by = 15
    queryset = Brand.objects.annotate(product_count = Count("product_brand"))

class BrandDetail(ListView):
    model = Product
    paginate_by = 20
    template_name = 'product/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count = Count("product_brand"))[0]
        return context
    
    
    
def querysetAPI(request):
    
    #data = Product.objects.select_related("brand").all() #prefetch_related = many-to-many
    
    #filter
    #data = Product.objects.filter(price__gte=30)#gt greater then , gte or equal
    #data = Product.objects.filter(price__range=(20,22))
    #relations
    #data = Product.objects.filter(brand__name="Apple")
    #filter with text
    #data = Product.objects.filter(name__contains="Ap")
    #data = Product.objects.filter(name__startswith="Ap") #endswith
    # data = Product.objects.filter(
    #     Q(price__lte = 23) &
    #     Q(quantity__lte = 5)
    # ) # you can  use Or , not(~) ...etc
    #data = Product.objects.filter(price = F('quantity'))
    #data = Product.objects.order_by('name')[0]
    #data = Product.objects.values('name','price','quantity','brand__name') #select colums
    #aggregate
    #data = Product.objects.aggregate(Sum('quantity'))
    #data = Product.objects.aggregate(Avg('price'))
    #annotate
    data = Product.objects.annotate(price_tva=F('price')*1.17)
    return render(request,"product/querysetApi.html",{"data":data})       
    
