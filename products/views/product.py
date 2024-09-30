from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from products.serializers import ProductSerializer, Product, CharacteristicsKey, CharacteristicsValue, ProductCharacteristics, CharacteristicsKeySerializer, CharacteristicsValueSerializer, ProductCharSerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from products.serializers import RegisterSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class ProductCreateAPI(CreateAPIView):
    serializer_class=ProductSerializer

class ProductListAPI(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
    #  return queryset.filter(owner=self.request.user)

class ProductUpdateAPI(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
        return super().perform_update(serializer)
    
class ProductRetrieveAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyAPI(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPI(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

class ProductRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)



class ProductRetrieveDestroyAPI(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class CharacteristicsKeyList(ListAPIView):
    queryset=CharacteristicsKey.objects.all()
    serializer_class=CharacteristicsKeySerializer

class CharacteristicsValueList(ListAPIView):
    queryset=CharacteristicsValue.objects.all()
    serializer_class=CharacteristicsValueSerializer

class ProductCharacteristicsList(ListAPIView):
    queryset=ProductCharacteristics.objects.all()
    serializer_class=ProductCharSerializer

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request, *args,**kwargs):
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)



class RegisterAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
               "user": UserSerializer(user).data,
               "token": token.key, 'created':created }, status=201)
    
   
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserLoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'created':created})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)