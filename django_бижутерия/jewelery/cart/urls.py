from django.urls import path
from .views import (
    add_to_cart,add_to_cart_in_cart,order_for_klient_delete,delete_product,delete_categorie,
    remove_from_cart,remove_from_cart_in_cart,
    view_cart,
    get_session_go_to_order_and_clear,OrderPageView
    )

app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('delete_categorie/<int:cat_id>/', delete_categorie, name='delete_categorie'),

    path('add/<int:product_id>/', add_to_cart_in_cart, name='add_to_cart_in_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove/<int:product_id>/', remove_from_cart_in_cart, name='remove_from_cart_in_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('order/', get_session_go_to_order_and_clear, name='get_session_go_to_order_and_clear'),
    path('order_page/', OrderPageView.as_view(), name='order_page'),
    path('order_klient_delete/<int:pk>/order_klient_delete/', order_for_klient_delete, name='order_for_klient_delete'),
]
