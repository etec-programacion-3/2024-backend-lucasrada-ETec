from django.db import models

# Create your models here.
class Product(models.Model):
    idProduct = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.IntegerField()

    def __str__(self):
        return self.name
class MusicProdDetails(models.Model):
    idProductDetails = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    users = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product Details {self.idProductDetails}"
class AudioProdDetails(models.Model):
    idProductDetails = models.AutoField(primary_key=True)
    neutral_sound = models.DecimalField(max_digits=10, decimal_places=1)
    sports = models.DecimalField(max_digits=10, decimal_places=1)
    gaming = models.DecimalField(max_digits=10, decimal_places=1)
    review = models.CharField(max_length=600)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Audio Details {self.idProductDetails}"
class OrderDetails(models.Model):
    idOrder = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.idOrder}"
class OrderItems(models.Model):
    idOrderItems = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderItem {self.idOrderItems}"
class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    full_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    full_address = models.CharField(max_length=75)

    def __str__(self):
        return self.username
class UserPayment(models.Model):
    idUserPayment = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=45)
    provider = models.CharField(max_length=45)
    account_no = models.CharField(max_length=45)
    expiry_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.idUserPayment}"
class MusicDiscography(models.Model):
    idDiscography = models.AutoField(primary_key=True)
    trackname = models.CharField(max_length=45)
    music_prod = models.ForeignKey(MusicProdDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.trackname
