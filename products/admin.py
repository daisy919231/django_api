from django.contrib import admin
from products.models import Category, Product, Group, Attribute, Value, Rating, Brand, Image
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Group)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Value)
admin.site.register(Rating)
admin.site.register(Brand)
admin.site.register(Image)


    