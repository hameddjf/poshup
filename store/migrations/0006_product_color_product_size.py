# Generated by Django 4.2.7 on 2024-02-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_concise'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='سفید', max_length=55),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='بزرگ', max_length=55),
        ),
    ]
