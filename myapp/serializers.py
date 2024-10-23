from rest_framework import serializers
from .models import Product, MusicProdDetails, AudioProdDetails, OrderDetails, OrderItems, User, UserPayment, MusicDiscography

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=45, required=True)
    desc = serializers.CharField(max_length=300, required=True)
    price = serializers.IntegerField()
    category = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'

class MusicProdDetailsSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    users = serializers.IntegerField()
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = MusicProdDetails
        fields = '__all__'

class AudioProdDetailsSerializer(serializers.ModelSerializer):
    neutral_sound = serializers.DecimalField(max_digits=10, decimal_places=1)
    sports = serializers.DecimalField(max_digits=10, decimal_places=1)
    gaming = serializers.DecimalField(max_digits=10, decimal_places=1)
    review = serializers.CharField(max_length=600)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = AudioProdDetails
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    user = serializers.PrimaryKeyRelatedField(queryset='User.objects.all()')

    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()
    order = serializers.PrimaryKeyRelatedField(queryset=OrderDetails.objects.all())

    class Meta:
        model = OrderItems
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=45, required=True)
    password = serializers.CharField(max_length=45, required=True)
    full_name = serializers.CharField(max_length=45, required=True)
    phone = serializers.CharField(max_length=15)
    full_address = serializers.CharField(max_length=75)

    class Meta:
        model = User
        fields = '__all__'

class UserPaymentSerializer(serializers.ModelSerializer):
    payment_type = serializers.CharField(max_length=45)
    provider = serializers.CharField(max_length=45)
    account_no = serializers.CharField(max_length=45)
    expiry_date = serializers.DateField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserPayment
        fields = '__all__'

class MusicDiscographySerializer(serializers.ModelSerializer):
    trackname = serializers.CharField(max_length=45)
    music_prod = serializers.PrimaryKeyRelatedField(queryset=MusicProdDetails.objects.all())

    class Meta:
        model = MusicDiscography
        fields = '__all__'

