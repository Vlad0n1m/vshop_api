from django.shortcuts import render
from .models import Family, ProductList, Product, ProductItem
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.http import require_GET
# Create your views here.
from .serializers import  FamilySerializer, ProductListSerializer, ProductSerializer, ProductItemSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class ProductListViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    
@require_GET
def get_family_by_owner(request, owner_id):
    try:
        family = Family.objects.get(owner_id=owner_id)
        # Assuming you have a serializer for your Family model
        # Replace `FamilySerializer` with your actual serializer
        serialized_family = FamilySerializer(family).data
        return JsonResponse(serialized_family, status=200)
    except Family.DoesNotExist:
        return JsonResponse({'error': 'Family not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)