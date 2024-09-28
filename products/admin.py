from django.contrib import admin
from products.models import Category, Product, Group, Rating, Brand, Image, Order, CharacteristicsKey, CharacteristicsValue, ProductCharacteristics
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Group)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group)

admin.site.register(CharacteristicsKey)
admin.site.register(CharacteristicsValue)
admin.site.register(ProductCharacteristics)
admin.site.register(Rating)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Order)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('base_title','slug')
    autocomplete_fields = ('is_liked',)