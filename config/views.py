from django.shortcuts import render
from product.models import Product, Brand, Review
from django.db.models import Count
# Create your views here.

def home(request):
    brands = Brand.objects.annotate(product_count = Count('product_brand'))
    sale_products = Product.objects.filter(flag ='Sale')[:10]
    new_products = Product.objects.filter(flag ='New')[:6]
    feature_products = Product.objects.filter(flag ='Features')[:10]
    reviews = Review.objects.filter(rate__gte = 4)[:5]
    print(feature_products)
    context = {
        "brands": brands,
        "sale_products": sale_products,
        "new_products": new_products,
        "feature_products": feature_products,
        "reviews":reviews

    }

    return render(request,"config/home.html", context)
