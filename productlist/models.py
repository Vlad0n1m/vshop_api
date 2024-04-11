from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_entity(sender, instance, created, **kwargs):
    if created:
        # Check if a profile already exists for this user
        if not hasattr(instance, 'profile'):
            profile = Profile(user=instance)
            profile.save()
        
# Create your models here.
class Family(models.Model):
    uid = models.UUIDField(max_length=255, default=uuid4(), unique=True, verbose_name='Уникальный идентификатор')
    owner = models.OneToOneField(Profile, verbose_name="Владелец семьи",  on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Название Семьи")
    
    def __str__(self) -> str:
        return f"Семья #{self.id} - '{self.name}'"

class ProductList(models.Model):
    family = models.ForeignKey(Family, related_name='product_lists',  on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", related_name='product_list')
    name = models.CharField(max_length=50, verbose_name='Название списка')
    date_created = models.DateTimeField(auto_created=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    price = models.IntegerField(verbose_name="Цена товара")
    
class ProductItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар',  on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество")
    date_created = models.DateTimeField(auto_created=True, verbose_name="Дата создания")
    who_added = models.ForeignKey(Profile, verbose_name="Пользователь добавивший", on_delete=models.CASCADE)
