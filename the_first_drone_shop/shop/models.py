import random
import string

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def rand_slug():
    """
    Generates a random slug consisting of lowercase letters and digits.

    Returns:
        str: A random slug.

    Example:
        >>> rand_slug()
        'abc123'
    """
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Название',max_length=250)
    supcategory = models.ForeignKey('self', on_delete=models.CASCADE,related_name='')
    slug = models.SlugField(verbose_name='URL',max_length=250,unique=True, null=False, editable=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    class Meta:
        unique_together = (['slug', 'parent'])
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        """
        Returns a string representation of the object.
        """
        full_path = [self.name]
        k = self.supcategory
        while k is not None:
            full_path.append(k.name)
            k = k.supcategory
        return ' > '.join(full_path[::-1])
    def save(self, *args, **kwargs):
        """
        Save the current instance to the database.
        """

        if not self.slug:
            self.slug = slugify(rand_slug() + '-pickBetter' + self.name)
        super(Category, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("shop:category-list", args=[str(self.slug)])

class Tags(models.Model):
    name = models.CharField(verbose_name='Название',max_length=50)
    slug = models.SlugField(max_length=255, unique=True,null=False, editable=True, db_index=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
     
    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(verbose_name='Название',max_length=250)
    brand = models.CharField(verbose_name='Бренд',max_length=250)
    description = models.TextField(verbose_name='Описание',blank=True)
    price = models.DecimalField(verbose_name='Цена',max_digits=8,decimal_places=2, default=0.00)
    image = models.ImageField(verbose_name='Изображение',upload_to='products/products/%Y/%m/%d')
    slug = models.SlugField(verbose_name='URL',max_length=250)
    available = models.BooleanField(verbose_name='Наличие',default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения',auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tags, blank=True, related_name='tags')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title



