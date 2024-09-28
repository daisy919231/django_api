import re
from django.db import models
from slugify import slugify
from uuslug import uuslug
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    base_title = models.CharField(max_length=255)  # Renamed to avoid clash

    class Meta:
        abstract = True  # Ensure this is an abstract model

class Category(BaseModel):
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __unicode__(self):
         return self.base_title

    def save(self, *args, **kwargs):
        if not self.slug and self.base_title:
            self.slug = uuslug(self.base_title, instance=self)
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

    def __unicode__(self):
         return self.base_title

    def save(self, *args, **kwargs):
        if not self.slug and self.base_title:
            self.slug = uuslug(self.base_title, instance=self)
        super(Group,self).save(*args, **kwargs)

    def __str__(self):
            return self.base_title

class Brand(BaseModel):
    location = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
            return self.base_title

# class Image(models.Model):
#     image = models.ImageField(null=True, blank=True)
    # is_primary = models.BooleanField(default=False)
    # def __str__(self):
    #         return self.image.url

# class Attribute(models.Model):
#     attribute = models.CharField(max_length=255)
#     def __str__(self):
#             return self.attribute

# class Value(models.Model):
#     value = models.CharField(max_length=255)
#     product_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
#     def __str__(self):
#             return self.value

class Product(BaseModel):
    price = models.FloatField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brands')
    is_liked = models.ManyToManyField(User, related_name='likes', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __unicode__(self):
         return self.base_title

    def save(self, *args, **kwargs):
        if not self.slug and self.base_title:
            self.slug = uuslug(self.base_title, instance=self)
        super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.base_title
    

class Image(models.Model):
     image=models.ImageField(upload_to='images/', null=True, blank=True)
     product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')
     is_primary = models.BooleanField(default=False)

     def __str__(self):
            return self.image.url
     

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='orders')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    first_payment = models.FloatField(null=True, blank=True, default=0)
    month = models.PositiveSmallIntegerField(default=3, null=True, blank=True,
                                             validators=[MinValueValidator(3), MaxValueValidator(12)])

    @property
    def monthly_payment(self):
        return self.product.price // self.month

    def __str__(self):
        return f'{self.product.name} - {self.user.username} - {self.quantity}'


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
    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='comments/', null=True, blank=True)


class CharacteristicsKey(models.Model):
    key_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
          return self.key_name

class CharacteristicsValue(models.Model):
    value_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
          return self.value_name


class ProductCharacteristics(models.Model):
    char_key=models.ForeignKey(CharacteristicsKey, on_delete=models.CASCADE, null=True, blank=True)
    char_value=models.ForeignKey(CharacteristicsValue, on_delete=models.CASCADE, null=True, blank=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='characteristics')

    class Meta:
         verbose_name_plural='ProductCharacteristics'

    def __str__(self):
          return f' {self.char_value.value_name} - {self.product.base_title} '