# urls.py
from django.urls import path
from books.views import BookListCreateAPIView, BookListAPIView, BookCreateAPIView

urlpatterns = [
    path('book_api/', BookListCreateAPIView.as_view(), name='book-list-create'),
    # path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('book_list/', BookListAPIView.as_view(), name='book_list' ),
    path('book_create/', BookCreateAPIView.as_view(), name='create_book'),
]
