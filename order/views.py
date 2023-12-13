

from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order,OrderDetail,Cart,CartDetail,Coupon
from product.models import Product

# Create your views here.

class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginated_by = 10

    def get_queryset(self):
        
        queryset = super().get_queryset().filter(user = self.request.user)
        return queryset

def add_to_cart(request):
    quantity = request.POST.get('quantity')
    product=Product.objects.get(id=request.POST.get('product_id'))
    cart=Cart.objects.get(user=request.user,status="InProgress")

    cart_detail,created= CartDetail.objects.get_or_create(cart=cart, product=product)

    cart_detail.quantity += int(quantity)
    cart_detail.total = round(cart_detail.quantity * product.price, 2)
    cart_detail.save()

    return redirect(f'/products/{product.slug}')



@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status="InProgress")
    cart_detail = CartDetail.objects.filter(cart=cart)

    return render(request,"order/checkout.html",{"cart_detail":cart_detail})