from django.urls import path
from products.views import category, groups, product
from rest_framework.authtoken import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('category_list/', cache_page(60*2)(category.CategoryListAPI.as_view()), name='category_list'),
    path('category_edit/<int:id>/', cache_page(60*2)(category.CategoryEditAPI.as_view()), name='category_edit'),
    path('category_list_simple/', cache_page(60*2)(category.CategoryListBase.as_view()), name='simple_category_list'),
    path('product_create_simple/', cache_page(60*2)(product.ProductCreateAPI.as_view()), name='simple_create'),
    path('product_list_simple/', cache_page(60*2)(product.ProductListAPI.as_view()), name='simple_list'),
    path('product_update_simple/<int:pk>/', cache_page(60*2)(product.ProductUpdateAPI.as_view()), name='simple_update'),
    path('product_delete_simple/<int:pk>/', cache_page(60*2)(product.ProductDestroyAPI.as_view()), name='simple_delete'),
    path('product_list_create/', cache_page(60*2)(product.ProductListCreateAPI.as_view()), name='list_create'),
    path('product_simple_retrieve/<int:pk>/', cache_page(60*2)(product.ProductRetrieveAPI.as_view()), name='simple_retrive'),
    path('product_retrieve_update/<int:pk>/', cache_page(60*2)(product.ProductRetrieveUpdateAPI.as_view()), name='retrive_update'),
    path('product_retrieve_delete/<int:pk>/', cache_page(60*2)(product.ProductRetrieveDestroyAPI.as_view()), name='retrieve_delete'),
    path('product_complex/<int:pk>/', cache_page(60*2)(product.ProductRetrieveUpdateDestroyAPI.as_view()), name='product_complex'),
    path('key_list/', cache_page(60*2)(product.CharacteristicsKeyList.as_view()), name='key_list'),
    path('value_list/', cache_page(60*2)(product.CharacteristicsValueList.as_view()), name='value_list' ),
    path('char_list/', cache_page(60*2)(product.ProductCharacteristicsList.as_view()), name='char_list'),
    path('api-token-auth/', views.obtain_auth_token),
    path('user_register/', cache_page(60*2)(product.RegisterAPI.as_view()), name='register'),
    path("get-details/", cache_page(60*2)(product.UserDetailAPI.as_view())),
    path('user_login/', cache_page(60*2)(product.UserLoginView.as_view()), name='login'),
    path('user_logout/', cache_page(60*2)(product.UserLogoutAPIView.as_view()), name='logout'),

]

# IMPORTANT!
# ALWAYS WRITE A PK IN THE URL, BECAUSE HOW DOES IT KNOW WHICH INSTANCE IT WANTS TO CHANGE?!