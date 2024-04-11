from django.shortcuts import render
from .models import ProductList, Product, ProductItem
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import ProductListSerializer, ProductSerializer, ProductItemSerializer
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
    
