# Generated by Django 4.1.5 on 2023-02-05 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_product_prodcut_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prodcut_status',
            new_name='product_status',
        ),
    ]