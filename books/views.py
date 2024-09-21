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



class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
    def get (self, request):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookCreateAPIView(APIView):
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