from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm
# Create your views here.





def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:all_news')  # Замените 'news_detail' на ваш urlpattern для деталей новости
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

def all_news(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'news/all_news.html', {'news_list': news_list})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})

def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('news:all_news')