import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Product, Brand

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
            brand = Brand.objects.get(id=random.randint(2,208)),
            subtitle = fake.text(max_nb_chars=90),
            description = fake.text(max_nb_chars=2000),
            flag = flags[random.randint(0,2)],
            price = round(random.uniform(20.99,99.99)),
            quantity = random.randint(0,50),
            sku = random.randint(1000,100000)          
        )
    
    print(f'seed {n} Brands')


seed_products(2000)

