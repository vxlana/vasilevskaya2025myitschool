from django.db import models
from unicodedata import category

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class ClothingItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sizes = models.ManyToManyField(Size, through='ClothingItemSize', related_name='clothing_items', blank=True)
    image = models.ImageField(upload_to='products/img', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clothing_items')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_price_with_discount(self):
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100))
        return self.price

class ClothingItemSize(models.Model):
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('clothing_item', 'size')


class Comment(models.Model):
    autor = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)









