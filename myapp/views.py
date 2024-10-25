from rest_framework import generics
from .models import Product, MusicProdDetails, AudioProdDetails, OrderDetails, OrderItems, User, UserPayment, MusicDiscography
from .serializers import ProductSerializer, MusicProdDetailsSerializer, AudioProdDetailsSerializer, OrderDetailsSerializer, OrderItemsSerializer, UserSerializer, UserPaymentSerializer, MusicDiscographySerializer

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# MusicProdDetails Views
class MusicProdDetailsListCreateView(generics.ListCreateAPIView):
    queryset = MusicProdDetails.objects.all()
    serializer_class = MusicProdDetailsSerializer

class MusicProdDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicProdDetails.objects.all()
    serializer_class = MusicProdDetailsSerializer

# AudioProdDetails Views
class AudioProdDetailsListCreateView(generics.ListCreateAPIView):
    queryset = AudioProdDetails.objects.all()
    serializer_class = AudioProdDetailsSerializer

class AudioProdDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioProdDetails.objects.all()
    serializer_class = AudioProdDetailsSerializer

# OrderDetails Views
class OrderDetailsListCreateView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

class OrderDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

# OrderItems Views
class OrderItemsListCreateView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

class OrderItemsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

# User Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# UserPayment Views
class UserPaymentListCreateView(generics.ListCreateAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer

class UserPaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer

# MusicDiscography Views
class MusicDiscographyListCreateView(generics.ListCreateAPIView):
    queryset = MusicDiscography.objects.all()
    serializer_class = MusicDiscographySerializer

class MusicDiscographyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicDiscography.objects.all()
    serializer_class = MusicDiscographySerializer
