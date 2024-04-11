from django.contrib import admin
from .models import Product, ProductItem, ProductList
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(ProductList)