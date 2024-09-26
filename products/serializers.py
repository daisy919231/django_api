from products.models import Category, Product
from rest_framework import serializers
from django.db.models import Avg

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
    all_images = serializers.SerializerMethodField()
    all_comments = serializers.SerializerMethodField()
    comment_count=serializers.SerializerMethodField()
    average_rating=serializers.SerializerMethodField()
    is_liked=serializers.SerializerMethodField()

    def get_all_images(self, instance):
        request = self.context.get('request')
        images = [request.build_absolute_uri(image.image.url) for image in instance.images.all()]
        return images
    
    

    def get_all_comments(self, instance):
        request = self.context.get('request')
        comments = [comment.message for comment in instance.ratings.all()]
        return comments
    
    def get_comment_count(self, instance):
        request = self.context.get('request')
        count=instance.ratings.count()
        return count
    
    def get_average_rating(self, instance):
        request = self.context.get('request')
        avg_rating=instance.ratings.aggregate(Avg('rating', default=0))
        return avg_rating
    
    def get_is_liked(self, instance):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return instance.is_liked.filter(id=user.id).exists()
        return False  
       

# a little inaccurate, because two names for average_rating, but I should look for a better solution!

    
    class Meta:
        model=Product
        fields='__all__'