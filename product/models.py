from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
FLAG_TYPES = (
    ('Sale','Sale'),
    ('Feature','Feature'),
    ('New','New')
)
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    sku = models.CharField(max_length=10)
    quantity = models.IntegerField()
    brand = models.ForeignKey("Brand", related_name='product_brand', on_delete=models.SET_NULL,null=True)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=4000)
    flag = models.CharField(choices=FLAG_TYPES,max_length=10)
    image = models.ImageField( upload_to='products', height_field=None, width_field=None, max_length=None)

class ProductImage(models.Model):
    pass

class Review(models.Model):
    user = models.ForeignKey(User,related_name="author_review'",on_delete=models.SET_NULL,null=True)
    Product = models.ForeignKey("Product", related_name='product_review', on_delete=models.CASCADE )
    review = models.TextField(max_length=1000)
    create_at = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(max=5)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image= models.ImageField(upload_to='brands', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name