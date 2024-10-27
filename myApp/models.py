from django.db import models

# Create your models here.

from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product)
