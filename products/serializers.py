from products.models import Category, Product, CharacteristicsKey, CharacteristicsValue, ProductCharacteristics
from rest_framework import serializers
from django.db.models import Avg
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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
        

class ProductCharSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCharacteristics
        exclude=('id', 'product', 'char_key', 'char_value')

    def to_representation(self, instance):
        context=super(ProductCharSerializer, self).to_representation(instance)
        # context['key_id']=instance.char_key.id
        # context['key_name']=instance.char_key.key_name
        # context['value_id']=instance.char_value.id
        # context['value_name']=instance.char_value.value_name
        # return context

        # ID KERAK BO'LSA YUQORIDAGI ISHLATILADI
        return {instance.char_key.key_name:instance.char_value.value_name}
    
        
    
class ProductSerializer(serializers.ModelSerializer):
    characteristics=ProductCharSerializer(many=True, read_only=True)
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


class CharacteristicsKeySerializer(serializers.ModelSerializer):
    class Meta:
        model=CharacteristicsKey
        fields='__all__'

class CharacteristicsValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=CharacteristicsValue
        fields='__all__'



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
