from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  FamilyViewSet, ProductListViewSet, ProductViewSet, ProductItemViewSet

router = DefaultRouter()
router.register(r'families', FamilyViewSet)
router.register(r'productlists', ProductListViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productitems', ProductItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

