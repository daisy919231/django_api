from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from products.serializers import Category, CategorySerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

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
