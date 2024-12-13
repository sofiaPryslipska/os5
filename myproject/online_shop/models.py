from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)

    def __str__(self):
        return self.title

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brands')

    def __str__(self):
        return self.name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=45)

    def __str__(self):
        return self.username



class Order(models.Model):
    order_status =[
        ('to ship', 'To Ship'),
        ('shipping', 'Shipping'),
        ('shipped', 'Shipped')]
    payment_status =[
        ('waiting', 'Waiting'),
        ('processing', 'Processing'),
        ('payed', 'Payed')]

    order_id = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=12, choices=order_status)
    price = models.FloatField()
    payment = models.CharField(max_length=12, choices=payment_status)
    address = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='order_users')


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_categories')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_categories')
    counter = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('product', 'category'),)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    counter = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('product', 'order'),)


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=45)
    card_cvv = models.CharField(max_length=3)
    expiration_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_users')

    def __str__(self):
        return self.card_number


