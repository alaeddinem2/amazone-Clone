from django.urls import path
from .views import OrderList,checkout,add_to_cart,remove_from_cart
from .api.api import CartDetailCreateAPI,OrderListAPI,OrderDetailAPI,CreateOrderAPI,ApplyCouponAPI

app_name = 'order'


urlpatterns = [
    path('',OrderList.as_view(),name= "orders"),
    path('checkout/',checkout,name= "checkout"), 
    path('add-to-cart',add_to_cart,name="add-to-cart"),
    path('<int:id>/remove-from-cart',remove_from_cart),


    #api
    #order
    path('api/list/<str:username>',OrderListAPI.as_view()),
    path('api/list/<str:username>/create-order',CreateOrderAPI.as_view()),
    path('api/<str:username>/<int:pk>',OrderDetailAPI.as_view()),

    #cart and coupon
    
    path('api/<str:username>/cart',CartDetailCreateAPI.as_view()),
    path('api/<str:username>/cart/apply-coupon',ApplyCouponAPI.as_view()),
    
]
