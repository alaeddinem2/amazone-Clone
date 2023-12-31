from rest_framework import serializers
from django.db.models.aggregates import Avg
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from ..models import Product, Review,Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class ProductListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    
    

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_avg = Avg('rate'))
        if not avg['rate_avg']:
            return 0
        return round(avg['rate_avg'])    
    
    def get_reviews_count(self,product):
        review_count = product.product_review.all().count()
        return review_count

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  

class ProductDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    reviews = ReviewSerializer(source ='product_review',many=True)
    

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_avg = Avg('rate'))
        if not avg['rate_avg']:
            return 0
        return round(avg['rate_avg'])    
    
    def get_reviews_count(self,product):
        review_count = product.product_review.all().count()
        return review_count
    
class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'