# Generated by Django 4.2 on 2023-09-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("logo", models.ImageField(upload_to="company", verbose_name="Logo")),
                ("subtitle", models.TextField(max_length=500, verbose_name="Subtitle")),
                ("fb_link", models.URLField(verbose_name="Facebook ")),
                ("tw_link", models.URLField(verbose_name="Twitter")),
                ("in_link", models.URLField(verbose_name="Linkedin")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=50, verbose_name="Phone")),
                ("address", models.CharField(max_length=50, verbose_name="Address")),
            ],
        ),
    ]