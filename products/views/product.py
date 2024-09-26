from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from products.serializers import Category, CategorySerializer, ProductSerializer, Product
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

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

