# Generated by Django 4.2 on 2023-12-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_brand_slug"),
        ("order", "0006_alter_order_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderdetail",
            old_name="quntity",
            new_name="quantity",
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_detail",
                to="order.order",
                verbose_name="Order",
            ),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="order_product",
                to="product.product",
                verbose_name="Product",
            ),
        ),
    ]
