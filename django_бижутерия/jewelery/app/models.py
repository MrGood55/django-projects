from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings
from django.db.models.query import QuerySet
from decimal import Decimal
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('app:category', kwargs={'cat_id': self.pk})
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    def __str__(self):
        return self.name








class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Order {self.product.name} by {self.user.username}"

    def get_cost(self):
        return self.price * self.quantity



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        MANAGER = "MANAGER", 'Manager'
        KLIENT = "KLIENT",'Klient'
    base_role = Role.ADMIN
    role = models.CharField(max_length=50,choices=Role.choices)

    def save(self, *args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)




class KlientManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs) -> QuerySet:
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.KLIENT)
    
# Klient.objects.create_user(username="",password="")
class Klient(User):
    base_role = User.Role.KLIENT
    klients = KlientManager()
    class Meta:
        proxy = True


class ManagerManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs) -> QuerySet:
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MANAGER)
    
# Manager.objects.create_user(username="",password="")
class Manager(User):
    base_role = User.Role.MANAGER
    managers = ManagerManager()
    class Meta:
        proxy = True