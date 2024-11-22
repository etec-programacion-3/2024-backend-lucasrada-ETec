from rest_framework import serializers
from .models import Product, ProductImage, MusicProdDetails, AudioProdDetails, OrderDetails, OrderItems, User, UserPayment, MusicDiscography
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=45, required=True)
    descri = serializers.CharField(max_length=300, required=True)
    price = serializers.IntegerField()

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
    email = serializers.EmailField(max_length=45, required=True)
    password = serializers.CharField(max_length=45, required=True)
    is_admin = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Invalid username or password")

        return {"user": user}  # En lugar de devolver solo datos básicos, devolvemos el usuario





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

class ProductImageSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  # O un 'StringRelatedField' si quieres mostrar el nombre del producto

    class Meta:
        model = ProductImage
        fields = ['id', 'product_id', 'image_url']  # Usamos 'image_url' en lugar de 'image'

