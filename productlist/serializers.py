from .models import ProductList, Product, ProductItem
from rest_framework import serializers
from django.contrib.auth.models import User
      


from rest_framework import serializers
from .models import ProductItem, ProductList, User, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'count', 'who_added',]
        read_only_fields = ['who_added']
        
    def create(self, validated_data):
        product_data = validated_data.pop('product')  # Извлекаем данные о продукте из валидированных данных
        product = Product.objects.create(**product_data)  # Создаем новый продукт
        product_item = ProductItem.objects.create(product=product, **validated_data)  # Создаем элемент продукта
        return product_item

class ProductListSerializer(serializers.ModelSerializer):
    products = ProductItemSerializer(many=True)
    members = UserSerializer(many=True)

    class Meta:
        model = ProductList
        fields = '__all__'