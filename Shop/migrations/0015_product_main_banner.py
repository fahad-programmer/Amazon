# Generated by Django 3.1.3 on 2020-11-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_remove_product_main_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_banner',
            field=models.ImageField(default=None, upload_to='Shop/images'),
        ),
    ]
