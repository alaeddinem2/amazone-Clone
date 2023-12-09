from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.utils.translation import gettext_lazy as _ 
from product.models import Product 
from utils.generate_code import generate_code
# Create your models here.
CART_STATUS = (
    ('InProgress','InProgress'),
    ('Completed','Completed')
)
ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'), 
)
class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='cart_user', on_delete=models.SET_NULL,blank=True,null=True)
    status = models.CharField(_("Status"), max_length=10, choices= CART_STATUS)

    def __str__(self):
        return str(self.user)
    
    def cart_total(self):
        total =0 
        for item in self.cart_detail.all():
            total+=item.total 

        return total

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Cart"),related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='cart_product', on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quantity"))
    total = models.FloatField(_("Total"))

    def __str__(self):
        return str(self.cart)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='order_user', on_delete=models.SET_NULL,blank=True,null=True)
    status = models.CharField(_("Status"), max_length=10, choices=ORDER_STATUS)
    code = models.CharField(_("Code"), max_length=50,blank=True,null=True)
    order_time = models.DateTimeField(_("Oder Time"), default=timezone.now)
    delivery_time = models.DateTimeField(_("Delivery Time"), null=True,blank=True)
    coupon = models.ForeignKey('Coupon', verbose_name=_("Coupon"),related_name='coupon_order', on_delete=models.SET_NULL,blank=True,null=True)
    total_after_coupon = models.FloatField(_("Total-Coupon"),blank=True,null=True)

    def __str__(self):
        return str(self.code)
    
    def save(self,*args, **kwargs):
        self.code = generate_code()
        super(Order,self).save(*args, **kwargs)

class OrderDetail(models.Model):
    order = models.ForeignKey(Cart, verbose_name=_("Order"),related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='oredr_product', on_delete=models.SET_NULL,blank=True,null=True)
    price = models.FloatField(_("Price"))
    quntity = models.IntegerField(_("Quantity"))
    total = models.FloatField(_("Total"))

    def __str__(self):
        return str(self.order)

class Coupon(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    discount = models.IntegerField(_("Discount"))
    quantity = models.IntegerField(_("Quantity"))
    start_date = models.DateTimeField(_("Start Date"),default=timezone.now)
    end_date = models.DateTimeField(_("End Date"),null=True,blank=True)

    def __str__(self):
        return str("Coupon code  "+self.code)

    
    
    def save(self,*args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        super(Coupon,self).save(*args, **kwargs)

    

