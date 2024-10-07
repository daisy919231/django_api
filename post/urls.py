from django.urls import path
from post.views import PostListView, PostDetailApiView,OnlyAdmin

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailApiView.as_view(), name='post_detail'),
    path('all-in-one/<int:pk>', OnlyAdmin.as_view(), name='all-in-one'),
]