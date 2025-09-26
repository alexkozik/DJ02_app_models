from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.

def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

# def create_news(request):
# 	form = NewsPostForm()
# 	return render(request, 'news/add_new_post.html', {'form': form})

def create_news(request):
    error=''
    if request.method == 'POST':
        # print(request.POST)
        form = NewsPostForm(request.POST) # Сюда сохранится информация от пользователя.
        if form.is_valid():
            # print(f"Вот такая форма {form}")
            form.save()
            return redirect('news_home')
        else:
            print(form.errors)
            error = "Данные были заполнены некорректно"
    form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})
