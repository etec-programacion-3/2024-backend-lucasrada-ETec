from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    MusicProdDetailsListCreateView, MusicProdDetailsDetailView,
    AudioProdDetailsListCreateView, AudioProdDetailsDetailView,
    OrderDetailsListCreateView, OrderDetailsDetailView,
    OrderItemsListCreateView, OrderItemsDetailView,
    UserListCreateView, UserDetailView,
    UserPaymentListCreateView, UserPaymentDetailView,
    MusicDiscographyListCreateView, MusicDiscographyDetailView,
    ProductImageDetailView, ProductImageListCreateView, ProductImageListView, SignUpView, LoginView
)

urlpatterns = [
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

     # ProductImage URLs
    # Ruta para acceder a las imágenes de un producto específico
    path('products/<int:product_id>/images/', ProductImageListCreateView.as_view(), name='product-image-list-create'),

    # Ruta para acceder a una imagen específica por su ID
    path('images/<int:pk>/', ProductImageDetailView.as_view(), name='product-image-detail'),

    # Ruta para acceder a todas las imágenes
    path('images/', ProductImageListView.as_view(), name='product-image-list'),


    # MusicProdDetails URLs
    path('music-products/', MusicProdDetailsListCreateView.as_view(), name='musicprod-list-create'),
    path('music-products/<int:pk>/', MusicProdDetailsDetailView.as_view(), name='musicprod-detail'),

    # AudioProdDetails URLs
    path('audio-products/', AudioProdDetailsListCreateView.as_view(), name='audioprod-list-create'),
    path('audio-products/<int:pk>/', AudioProdDetailsDetailView.as_view(), name='audioprod-detail'),

    # OrderDetails URLs
    path('orders/', OrderDetailsListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailsDetailView.as_view(), name='order-detail'),

    # OrderItems URLs
    path('order-items/', OrderItemsListCreateView.as_view(), name='order-items-list-create'),
    path('order-items/<int:pk>/', OrderItemsDetailView.as_view(), name='order-items-detail'),

    # User URLs
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # UserPayment URLs
    path('user-payments/', UserPaymentListCreateView.as_view(), name='user-payment-list-create'),
    path('user-payments/<int:pk>/', UserPaymentDetailView.as_view(), name='user-payment-detail'),

    # MusicDiscography URLs
    path('music-discography/', MusicDiscographyListCreateView.as_view(), name='music-discography-list-create'),
    path('music-discography/<int:pk>/', MusicDiscographyDetailView.as_view(), name='music-discography-detail'),
    
    #

]
