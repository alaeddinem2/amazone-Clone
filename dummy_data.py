import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Product, Brand, Review,ProductImage
from django.contrib.auth.models import User

def seed_brands(n):
    fake = Faker()
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brands/{images[random.randint(0,9)]}'
        )
    
    print(f'seed {n} Brands')

def seed_products(n):
    fake = Faker()
    flags = ['New','Features','Sale']
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{images[random.randint(0,9)]}',
            brand = Brand.objects.get(id=random.randint(1,50)),
            subtitle = fake.text(max_nb_chars=90),
            description = fake.text(max_nb_chars=2000),
            flag = flags[random.randint(0,2)],
            price = round(random.uniform(20.99,99.99)),
            quantity = random.randint(0,50),
            sku = random.randint(1000,100000)          
        )
def seed_reviews(n):
    fake = Faker()
    flags = ['New','Features','Sale']
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    for _ in range(n):
        Review.objects.create(
            
            user = User.objects.get(id=random.randint(1,7)),
            Product = Product.objects.get(id=random.randint(1,3000)),
            review = fake.text(max_nb_chars=100),
            rate = random.randint(0,5),
                      
        )    
    print(f'seed {n} Brands')

def seed_images():
    fake = Faker()
    flags = ['New','Features','Sale']
    images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    for n in range(1,3000):
        for _ in range(3):
            ProductImage.objects.create( 
                product = Product.objects.get(id=n),
                image = f'products/{images[random.randint(0,9)]}',
                
                
                        
            )    
    print(f'seed {n} Brands')


seed_images()

