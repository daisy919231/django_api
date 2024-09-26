from django.urls import path
from products.views import category, groups, product

urlpatterns = [
    path('category_list/', category.CategoryListAPI.as_view(), name='category_list'),
    path('category_edit/<int:id>/', category.CategoryEditAPI.as_view(), name='category_edit'),
    path('category_list_simple/', category.CategoryListBase.as_view(), name='simple_category_list'),
    path('product_create_simple/', product.ProductCreateAPI.as_view(), name='simple_create'),
    path('product_list_simple/', product.ProductListAPI.as_view(), name='simple_list'),
    path('product_update_simple/<int:pk>/', product.ProductUpdateAPI.as_view(), name='simple_update'),
    path('product_delete_simple/<int:pk>/', product.ProductDestroyAPI.as_view(), name='simple_delete'),
    path('product_list_create/', product.ProductListCreateAPI.as_view(), name='list_create'),
    path('product_simple_retrieve/<int:pk>/', product.ProductRetrieveAPI.as_view(), name='simple_retrive'),
    path('product_retrieve_update/<int:pk>/', product.ProductRetrieveUpdateAPI.as_view(), name='retrive_update'),
    path('product_retrieve_delete/<int:pk>/', product.ProductRetrieveDestroyAPI.as_view(), name='retrieve_delete'),
    path('product_complex/<int:pk>/', product.ProductRetrieveUpdateDestroyAPI.as_view(), name='product_complex')
    

]

# IMPORTANT!
# ALWAYS WRITE A PK IN THE URL, BECAUSE HOW DOES IT KNOW WHICH INSTANCE IT WANTS TO CHANGE?!