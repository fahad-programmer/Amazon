# Generated by Django 3.1.3 on 2020-11-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0016_auto_20201123_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delievery_Date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
