from django.shortcuts import render
from .models import ProductList, Product, ProductItem
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import ProductListSerializer, ProductSerializer, ProductItemSerializer, UserSerializer
from rest_framework import generics, permissions

class ProductListViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    
class UserProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductList.objects.filter(owner=user)



class IsOwnerOrMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Пользователь является владельцем или участником списка продуктов
        return obj.owner == request.user or request.user in obj.members.all()

class ProductListDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrMember] 

    def get_object(self):
        uid = self.kwargs['uid']
        # Получение объекта ProductList по uid
        obj = ProductList.objects.filter(uid=uid).first()
        return obj
    


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ProductList, ProductItem
from .serializers import ProductListSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def get_product_list(request, uid):
    """
    Получение данных списка вместе с продуктами и пользователями.
    """
    product_list = get_object_or_404(ProductList, uid=uid)
    serializer = ProductListSerializer(product_list)
    return Response(serializer.data)

@api_view(['POST'])
def add_product_to_list(request, uid):
    """
    Добавление продукта в список.
    """
    if request.method == 'POST':
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            # Получаем экземпляр ProductList по uid
            product_list = get_object_or_404(ProductList, uid=uid)
            # Создаем ProductItem с переданными данными
            product_item = serializer.save(who_added=request.user)
            # Добавляем ProductItem в список
            product_list.products.add(product_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_member_to_list(request, uid):
    """
    Добавление пользователя в ProductList.
    """
    product_list = get_object_or_404(ProductList, uid=uid)
    username = request.data.get('username')
    user_to_add = get_object_or_404(User, username=username)
    product_list.members.add(user_to_add)
    product_list.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product_list_users(request, uid):
    """
    Получение всех пользователей списка.
    """
    product_list = get_object_or_404(ProductList, uid=uid)
    users = product_list.members.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_list_products(request, uid):
    """
    Получение всех продуктов списка.
    """
    product_list = get_object_or_404(ProductList, uid=uid)
    products = product_list.products.all()
    serializer = ProductItemSerializer(products, many=True)
    return Response(serializer.data)