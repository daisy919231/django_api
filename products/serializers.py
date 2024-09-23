from products.models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
    
    def groups_count(self, obj):
        count=obj.groups.count()
        return count
    
    def get_full_image_url(self, instance):
        if instance.image:
            image_url=instance.image.url
            request=self.context.get('request')
            return request.build_absolute_url(image_url)
        else:
            return None
        
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'