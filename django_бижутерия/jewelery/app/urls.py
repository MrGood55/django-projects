



from django.urls import path

from .views import (
    ProductListView, ProductDetailView,ProductCategory,about,
    AddProductView,
    register_klient, LoginUser, logout_user,register_user_by_admin,user_list,delete_user,
    OrderListView, order_delete,
)
app_name = 'app'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', ProductCategory.as_view(), name='category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('register_klient/', register_klient, name='register_klient'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register_user_by_admin/', register_user_by_admin, name='register_user_by_admin'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/delete/', order_delete, name='order_delete'),
    path('user/', user_list, name='user_list'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),

    
]
