from django.contrib import admin

# Register your models here.
from .models import Product,Review,ProductImage,Brand

class ProductImageTabulair(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','price','quantity','flag','sku']
    list_filter = ['brand','name','price']
    #list_editable = ['price']
    inlines = [ProductImageTabulair]
    search_fields = ['name']


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Brand)