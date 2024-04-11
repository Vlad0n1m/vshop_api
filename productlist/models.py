from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
import random, string
import datetime

class ProductList(models.Model):
    products = models.ManyToManyField("ProductItem", related_name='product_list', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='Название списка')
    date_created = models.DateTimeField(auto_created=True, default=datetime.datetime.now(), blank=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    uid = models.CharField(max_length=100, verbose_name='Кастомная ссылка', blank=True, default=uuid4(), unique=True)
    owner = models.ForeignKey(User, related_name='product_lists', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='shared_product_lists', blank=True)
    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    price = models.IntegerField(verbose_name="Цена товара")
    origin = models.CharField(max_length=255, verbose_name='Провайдер', default='default')
    
class ProductItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар',  on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество")
    image = models.ImageField(upload_to='product_item_images', verbose_name='Картинка', null=True, blank=True)
    date_created = models.DateTimeField(auto_created=True, verbose_name="Дата создания")
    who_added = models.ForeignKey(User, verbose_name="Пользователь добавивший", on_delete=models.CASCADE)
