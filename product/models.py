from collections.abc import Iterable
from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
FLAG_TYPES = (
    ('Sale','Sale'),
    ('Feature','Feature'),
    ('New','New')
)
class Product(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    price = models.FloatField(_("Price"))
    sku = models.CharField(_("SKU"),max_length=10)
    quantity = models.IntegerField(_("Quantity"))
    brand = models.ForeignKey("Brand", related_name='product_brand',verbose_name=_("Brand"), on_delete=models.SET_NULL,null=True)
    subtitle = models.CharField(_("Subtitle"),max_length=300)
    description = models.TextField(_("Description"),max_length=4000)
    flag = models.CharField(_("Flag"),choices=FLAG_TYPES,max_length=10)
    image = models.ImageField( _("Image"),upload_to='products', height_field=None, width_field=None, max_length=None)
    tags = TaggableManager()
    slug = models.SlugField(_("Slug"), null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey("Product",related_name='product_image',verbose_name=_("Product"),on_delete=models.CASCADE)
    image = models.ImageField( _("Image"),upload_to="product_images", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.product)

class Review(models.Model):
    user = models.ForeignKey(User,related_name="author_review",verbose_name=_("Author"),on_delete=models.SET_NULL,null=True)
    Product = models.ForeignKey("Product", related_name='product_review',verbose_name=_("Product"), on_delete=models.CASCADE )
    review = models.TextField(_("Review"),max_length=1000)
    create_at = models.DateTimeField(_("Create At"),default=timezone.now)
    rate = models.IntegerField(_("Rate"))

    def __str__(self):
        
        return  str(self.user) +" " + str(self.Product) + "  review"
    

class Brand(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    image= models.ImageField(_("Image"),upload_to='brands', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name