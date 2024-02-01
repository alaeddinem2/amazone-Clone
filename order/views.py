

from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order,OrderDetail,Cart,CartDetail,Coupon
from product.models import Product
from django.shortcuts import get_object_or_404
from django.utils import timezone
from config.models import DeleveryFee
from django.http import JsonResponse
from django.template.loader import render_to_string
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

    cart_detail.quantity = int(quantity)
    cart_detail.total = round(cart_detail.quantity * product.price, 2)
    cart_detail.save()

    return redirect(f'/products/{product.slug}')

def remove_from_cart(request,id):
    cart_detail = CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/products/')

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status="InProgress")
    cart_detail = CartDetail.objects.filter(cart=cart)
    delevery_fee = DeleveryFee.objects.last().fee
    print(delevery_fee)

    if request.method == "POST":
        coupon = get_object_or_404(Coupon,code = request.POST['coupon_code'])
        if coupon and coupon.quantity >0 :
            today_date = timezone.now()

            if today_date >= coupon.start_date and today_date <= coupon.end_date :
                coupon_value = cart.cart_total() * coupon.discount/100
                cart_total = cart.cart_total() - coupon_value
                coupon.quantity -= 1
                coupon.save()

                cart.coupon = coupon
                cart.total_after_coupon = cart_total
                cart.save()
                cart= Cart.objects.get(user=request.user,status = "InProgress")

                html = render_to_string('include/checkout_table.html',{
                                        "cart_detail":cart_detail,
                                        "sub_total":cart_total,
                                        "discount":coupon_value,
                                        "delevery_fee": delevery_fee,
                                        "total":delevery_fee + cart_total

                                        })
                return JsonResponse({'result':html})

               
                
    
    else:
        sub_total = cart.cart_total()
        total = delevery_fee + sub_total
        
        return render(request,"order/checkout.html",{
                    "cart_detail":cart_detail,
                    "sub_total":sub_total,
                    "discount":0,
                    "delevery_fee": delevery_fee,
                    "total":total

                    },)