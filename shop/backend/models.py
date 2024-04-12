from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(verbose_name='description')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    desc=models.TextField(verbose_name='description')
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='products')
    def __str__(self) -> str:
        return f'{self.name} {self.price}'
    
    class Meta:
        verbose_name_plural='Products'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=PhoneNumberField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    total_prices=models.FloatField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)