from django.urls import path,include
from .views import ProductList , ProductDetail, BrandList,BrandDetail, querysetAPI,add_review
from .api.api import product_list_api,product_detail_api,ProductDetailApi,ProductListApi, BrandDetailApi, BrandListApi, ReviewDetailApi, ReviewListApi

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view() ),
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    path('test/',querysetAPI),
    path('<slug:slug>/add_review',add_review,name='add_review'),
    path('api/list',ProductListApi.as_view()),
    path('api/<int:pk>',ProductDetailApi.as_view()),
    path('api/brand-list',BrandListApi.as_view()),
    path('api/brands/<int:pk>',BrandDetailApi.as_view()),
    path('api/reviews-list',ReviewListApi.as_view()),
    path('api/review/<int:pk>',ReviewDetailApi.as_view())
    
]