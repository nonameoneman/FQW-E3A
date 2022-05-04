from django.shortcuts import render, redirect


def news_a(request):
    return render(request, 'app_news/news_a.html', {'title':'Управление новостями'})

def news_s(request):
    return render(request, 'app_news/news_s.html', {'title':'Новости'})