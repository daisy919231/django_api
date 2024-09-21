from django.urls import path
from products.views import CategoryListAPI, CategoryEditAPI

urlpatterns = [
    path('category_list/', CategoryListAPI.as_view(), name='category_list'),
    path('category_edit/<int:id>/', CategoryEditAPI.as_view(), name='category_edit'),
]