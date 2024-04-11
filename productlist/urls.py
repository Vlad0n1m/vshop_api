from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_family_by_owner, FamilyViewSet, ProductListViewSet, ProductViewSet, ProductItemViewSet

router = DefaultRouter()
router.register(r'families', FamilyViewSet)
router.register(r'productlists', ProductListViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productitems', ProductItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/family/<int:owner_id>/', get_family_by_owner, name='get_family_by_owner'),

]

