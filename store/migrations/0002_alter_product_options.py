# Generated by Django 4.2.5 on 2023-11-09 17:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "محصول", "verbose_name_plural": "محصولات"},
        ),
    ]
