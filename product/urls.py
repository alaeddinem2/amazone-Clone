from django.urls import path,include
from .views import ProductList , ProductDetail, BrandList,BrandDetail, querysetAPI
from .API.api import product_list_api,product_detail_api,ProductDetailApi,ProductListApi
app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view() ),
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    path('test/',querysetAPI),
    path('api/list',ProductListApi.as_view()),
    path('api/<int:pk>',ProductDetailApi.as_view())
    
]