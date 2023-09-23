from django.urls import path
from .views import ProductList , ProductDetail

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    
]