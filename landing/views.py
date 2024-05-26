from django.shortcuts import render
from core.models import News
from datetime import datetime, timedelta


def index(request):
    # Получаем дату, предшествующую сегодняшнему дню на 7 дней
    week_ago = datetime.now() - timedelta(days=7)
    # Получаем все новости, опубликованные за последнюю неделю
    latest_news = News.objects.filter(date__gte=week_ago)
    return render(request, "landing/index.html", {"latest_news": latest_news})


def about(request):
    return render(request, "landing/about.html")


def news(request):
    # Получаем дату, предшествующую сегодняшнему дню на 7 дней
    week_ago = datetime.now() - timedelta(days=7)
    # Получаем все новости, опубликованные за последнюю неделю
    latest_news = News.objects.filter(date__gte=week_ago)
    return render(request, "landing/news.html", {"latest_news": latest_news})