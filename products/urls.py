from django.urls import path
from products.views import category, groups, product
from rest_framework.authtoken import views

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
    path('product_complex/<int:pk>/', product.ProductRetrieveUpdateDestroyAPI.as_view(), name='product_complex'),
    path('key_list/', product.CharacteristicsKeyList.as_view(), name='key_list'),
    path('value_list/', product.CharacteristicsValueList.as_view(), name='value_list' ),
    path('char_list/', product.ProductCharacteristicsList.as_view(), name='char_list'),
    path('api-token-auth/', views.obtain_auth_token),
    path('user_register/',product.RegisterAPI.as_view(), name='register'),
    path("get-details/", product.UserDetailAPI.as_view()),
    path('user_login/', product.UserLoginView.as_view(), name='login'),
    path('user_logout/', product.UserLogoutAPIView.as_view(), name='logout'),

]

# IMPORTANT!
# ALWAYS WRITE A PK IN THE URL, BECAUSE HOW DOES IT KNOW WHICH INSTANCE IT WANTS TO CHANGE?!