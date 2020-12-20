from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=200 , null=True)
    phone = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.name
def create_customer(sender,instance , created , **kwargs):
    if created:
        Customer.objects.create(user = instance)
post_save.connect(create_customer , sender =User )


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY =(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200 , null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200 , null=True,choices=CATEGORY)
    description = models.CharField(max_length=200 , null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True , choices=STATUS)
