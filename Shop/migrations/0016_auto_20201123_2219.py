# Generated by Django 3.1.3 on 2020-11-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_product_main_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]