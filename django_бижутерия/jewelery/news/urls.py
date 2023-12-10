

from django.urls import path
from .views import (
    add_news,
    all_news,
    news_detail,
    delete_news
)

app_name = 'news'
urlpatterns = [
    # Ваши существующие urlpatterns
    path('add_news/', add_news, name='add_news'),
    path('all_news/', all_news, name='all_news'),
    path('news_detail/<int:pk>/', news_detail, name='news_detail'),
    path('delete_news/<int:pk>/', delete_news, name='delete_news'),
]
