# Generated by Django 4.2 on 2023-09-05 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='brands', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('sku', models.CharField(max_length=10, verbose_name='SKU')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('description', models.TextField(max_length=4000, verbose_name='Description')),
                ('flag', models.CharField(choices=[('Sale', 'Sale'), ('Feature', 'Feature'), ('New', 'New')], max_length=10, verbose_name='Flag')),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='product.brand', verbose_name='Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000, verbose_name='Review')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create At')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.product', verbose_name='Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_review', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='Product')),
            ],
        ),
    ]