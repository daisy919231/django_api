from django.contrib import admin
from products.models import Category, Product, Group, Attribute, Value, Rating, Brand, Image
# Register your models here.
admin.site.register(Category)
admin.site.register(Group)