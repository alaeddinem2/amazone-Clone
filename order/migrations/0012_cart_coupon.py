# Generated by Django 4.2 on 2024-01-20 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0011_alter_cartdetail_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="coupon_cart",
                to="order.coupon",
                verbose_name="Coupon",
            ),
        ),
    ]
