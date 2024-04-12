# Generated by Django 5.0.4 on 2024-04-12 06:44

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0002_alter_productlist_date_created_alter_productlist_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='date_created',
            field=models.DateTimeField(auto_created=True, blank=True, default=datetime.datetime(2024, 4, 12, 11, 44, 34, 377344), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='uid',
            field=models.CharField(blank=True, default=uuid.UUID('72a57774-f808-45d5-9cec-4d3335edc5ef'), max_length=100, unique=True, verbose_name='Кастомная ссылка'),
        ),
    ]
