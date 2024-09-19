# urls.py
from django.urls import path
from books.views import BookListCreateAPIView

urlpatterns = [
    path('book_api/', BookListCreateAPIView.as_view(), name='book-list-create'),
    # path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
