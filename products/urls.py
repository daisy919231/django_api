from django.urls import path
from products.views import CategoryListAPI, CategoryEditAPI, CategoryListBase, ProductCreateAPI, ProductListAPI, ProductUpdateAPI, ProductDestroyAPI, ProductRetrieveDestroyAPI, ProductListCreateAPI, ProductRetrieveAPI, ProductRetrieveUpdateAPI, ProductRetrieveUpdateDestroyAPI

urlpatterns = [
    path('category_list/', CategoryListAPI.as_view(), name='category_list'),
    path('category_edit/<int:id>/', CategoryEditAPI.as_view(), name='category_edit'),
    path('category_list_simple/', CategoryListBase.as_view(), name='simple_category_list'),
    path('product_create_simple/', ProductCreateAPI.as_view(), name='simple_create'),
    path('product_list_simple/', ProductListAPI.as_view(), name='simple_list'),
    path('product_update_simple/<int:pk>/', ProductUpdateAPI.as_view(), name='simple_update'),
    path('product_delete_simple/<int:pk>/', ProductDestroyAPI.as_view(), name='simple_delete'),
    path('product_list_create/', ProductListCreateAPI.as_view(), name='list_create'),
    path('product_simple_retrieve/<int:pk>/', ProductRetrieveAPI.as_view(), name='simple_retrive'),
    path('product_retrieve_update/<int:pk>/', ProductRetrieveUpdateAPI.as_view(), name='retrive_update'),
    path('product_retrieve_delete/<int:pk>/', ProductRetrieveDestroyAPI.as_view(), name='retrieve_delete'),
    path('product_complex/<int:pk>/', ProductRetrieveUpdateDestroyAPI.as_view(), name='product_complex')
    

]

# IMPORTANT!
# ALWAYS WRITE A PK IN THE URL, BECAUSE HOW DOES IT KNOW WHICH INSTANCE IT WANTS TO CHANGE?!