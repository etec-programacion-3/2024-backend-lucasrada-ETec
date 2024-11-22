from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    descri = models.CharField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name
class MusicProdDetails(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    users = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product Details {self.idProductDetails}"
class AudioProdDetails(models.Model):
    id = models.AutoField(primary_key=True)
    neutral_sound = models.DecimalField(max_digits=10, decimal_places=1)
    sports = models.DecimalField(max_digits=10, decimal_places=1)
    gaming = models.DecimalField(max_digits=10, decimal_places=1)
    review = models.CharField(max_length=600)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Audio Details {self.idProductDetails}"
class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.idOrder}"
class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderItem {self.idOrderItems}"

#################-----  Modificaciones para login y register mas seguros y mejores y tal -----##################
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        extra_fields.setdefault('is_admin', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(default='example@example.com')
    password = models.CharField(max_length=128, default='defaultpassword')
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
##################################################################################################################


class UserPayment(models.Model):
    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=45)
    provider = models.CharField(max_length=45)
    account_no = models.CharField(max_length=45)
    expiry_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.idUserPayment}"
class MusicDiscography(models.Model):
    id = models.AutoField(primary_key=True)
    trackname = models.CharField(max_length=45)
    music_prod = models.ForeignKey(MusicProdDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.trackname


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(null=True)  # Almacena la URL de la imagen

    def __str__(self):
        return f"Image  for {self.product_id.name}"