from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    img_url = models.CharField(max_length=255)
