from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from products.serializers import Category, CategorySerializer, ProductSerializer, Product
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class CategoryListAPI(APIView):
    def get(self, request):
        category=Category.objects.all()
        serializer=CategorySerializer(category, many=True)
        return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryEditAPI(APIView):
    def get(self, request, id=None, **kwargs):
        category=get_object_or_404(Category, id=id)
        serializer=CategorySerializer(category)
        return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)

        
    def patch(self,request, id=None):
        category=Category.objects.get(id=id)
        serializer=CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id, **kwargs):
        category=get_object_or_404(Category, id=id)
        category.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    

class CategoryListBase(APIView):
    def get(self, request):
        # data = {
        #     category.id: {
        #         'title': category.base_title,
        #         'slug': category.slug,
        #     }
        #     for category in Category.objects.all()
        # }
        #2ND VERSION
        # data = dict((category.id, {'title': category.base_title, 'slug': category.slug})
        # for category in Category.objects.all()

        #3RD VERSION
        # data = {}
        # for category in Category.objects.all():
        #     data[category.slug] = {
        #         'title': category.base_title,
        #         'slug': category.slug,
        #         }
        # # base_title did not work here!


        # 4th VERSION
        categories = Category.objects.values('id', 'base_title', 'slug')
        data = {category['base_title']: {'title': category['base_title'], 'slug': category['slug']} for category in categories}

            


        return Response(data, status=status.HTTP_200_OK)
    