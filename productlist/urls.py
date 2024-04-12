from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListViewSet, ProductViewSet, ProductItemViewSet, UserProductListView, ProductListDetailAPIView
from .views import get_product_list, add_product_to_list, add_member_to_list, get_product_list_products
router = DefaultRouter()
router.register(r'productlists', ProductListViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productitems', ProductItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user-product-lists/', UserProductListView.as_view(), name="user-product-lists"),
    path('product-list/<str:uid>/', ProductListDetailAPIView.as_view(), name='product-list-detail'),
     path('lists/<str:uid>/', get_product_list, name='get_product_list'),
    path('lists/<str:uid>/add_product/', add_product_to_list, name='add_product_to_list'),
    path('lists/<str:uid>/products/', get_product_list_products, name='get_product_list_products'),
    path('lists/<str:uid>/add_member/', add_member_to_list, name='add_member_to_list'),
]

