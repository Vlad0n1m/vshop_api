from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListViewSet, ProductViewSet, ProductItemViewSet, UserProductListView, ProductListDetailAPIView

router = DefaultRouter()
router.register(r'productlists', ProductListViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productitems', ProductItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user-product-lists/', UserProductListView.as_view(), name="user-product-lists"),
    path('product-list/<str:uid>/', ProductListDetailAPIView.as_view(), name='product-list-detail'),
]

