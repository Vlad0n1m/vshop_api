from django.contrib import admin
from .models import Profile, Product, ProductItem, ProductList, Family
# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(ProductList)
admin.site.register(Family)