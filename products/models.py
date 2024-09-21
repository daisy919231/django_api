import re
from django.db import models
from django.utils.text import slugify


def custom_slugify(value):
    # Convert to lowercase
    value = value.lower()
    # Remove any special characters except for spaces and hyphens
    value = re.sub(r'[^\w\s-]', '', value)
    # Replace spaces and consecutive hyphens with a single hyphen
    value = re.sub(r'[-\s]+', '-', value).strip('-')
    return value

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    base_title = models.CharField(max_length=100)  # Renamed to avoid clash

    class Meta:
        abstract = True  # Ensure this is an abstract model

class Category(BaseModel):
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.base_title:
            self.slug = custom_slugify(self.base_title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Categories'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.base_title

class Group(BaseModel):
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='groups')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=custom_slugify(self.base_title)
        super(Group,self).save(*args, **kwargs)

    def __str__(self):
            return self.base_title

class Brand(BaseModel):
    location = models.CharField(max_length=255, null=True, blank=True)

class Image(models.Model):
    image = models.ImageField(null=True, blank=True)
    is_primary = models.BooleanField(default=False)

class Attribute(models.Model):
    attribute = models.CharField(max_length=255)

class Value(models.Model):
    value = models.CharField(max_length=255)
    product_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

class Product(BaseModel):
    price = models.FloatField(default=25)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='products')
    product_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name='product_values')
    description = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brands')
    is_liked = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=custom_slugify(self.base_title)
        super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.base_title

class Rating(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
