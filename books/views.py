from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# FOR SWAGGER

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# caching
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.core.cache import cache


# @method_decorator(cache_page(60 * 60 * 2), name='dispatch')
# @method_decorator(vary_on_headers("Authorization"))
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        cache_key='book_list'
        cached_data=cache.get(cache_key)
        if not cached_data:
            queryset=Book.objects.all().select_related('author')
            cache.set(cache_key, queryset, timeout=60*3)
            return queryset
        return cached_data




class MyAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get a list of items",
        responses={200: openapi.Response('Success', BookSerializer(many=True))}
    )
    def get(self, request):
        items = Book.objects.all()
        serializer = BookSerializer(items, many=True)
        return Response(serializer.data)

# class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in Book.objects.all()]
#         return Response(usernames)

class BookListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self, request):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self, request):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data= {
                'success':True,
                'message':'Book created succesfully'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)