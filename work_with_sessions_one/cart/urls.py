"""
URL configuration for work_with_sessions_one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
index,
get_to_cart,get_to_cart_for_btn,
clear_cart,
plus_item,plus_item_btn,
minus_item,minus_item_btn

)

app_name = 'cart'
urlpatterns = [
    ###todo detail by slug
    path('', index,name='shopping_cart'),

    path('get_to_cart/<int:item_pk>', get_to_cart, name='get_to_cart'),
    path('get_to_cart_for_btn/', get_to_cart_for_btn, name='get_to_cart_for_btn'),

    path('plus_item/<int:item_pk>', plus_item, name='plus_item'),
    path('plus_item_btn/', plus_item_btn, name='plus_item_btn'),

    path('minus_item/<int:item_pk>', minus_item, name='minus_item'),
    path('minus_item_btn', minus_item_btn, name='minus_item_btn'),

    path('clear_cart/', clear_cart, name='clear_cart'),


]
