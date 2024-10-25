from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    MusicProdDetailsListCreateView, MusicProdDetailsDetailView,
    OrderDetailsListCreateView, OrderDetailsDetailView,
    # Include other views as needed...
)

urlpatterns = [
    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # MusicProdDetails URLs
    path('music-products/', MusicProdDetailsListCreateView.as_view(), name='musicprod-list-create'),
    path('music-products/<int:pk>/', MusicProdDetailsDetailView.as_view(), name='musicprod-detail'),

    # OrderDetails URLs
    path('orders/', OrderDetailsListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailsDetailView.as_view(), name='order-detail'),

    # Add URLs for other models...
]
