from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class  Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name


class Bike(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bike_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    color_type = models.ForeignKey(ColorVariant, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.bike_name


