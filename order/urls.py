from django.urls import path
from .views import OrderList,checkout,add_to_cart,remove_from_cart

app_name = 'order'


urlpatterns = [
    path('',OrderList.as_view()),
    path('checkout/',checkout),
    path('add-to-cart',add_to_cart,name="add-to-cart"),
    path('<int:id>/remove-from-cart',remove_from_cart),
]
