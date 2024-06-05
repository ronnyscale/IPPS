from django.shortcuts import render, get_object_or_404
from core.models import News
from datetime import datetime, timedelta
from core.models import Department, Partner


def index(request):
    # Получаем дату, предшествующую сегодняшнему дню на 7 дней
    week_ago = datetime.now() - timedelta(days=31)
    # Получаем все новости, опубликованные за последнюю неделю
    latest_news = News.objects.filter(date__gte=week_ago)
    return render(request, "landing/index.html", {"latest_news": latest_news})


def about(request):
    return render(request, "landing/about.html")


def news(request):
    # Получаем дату, предшествующую сегодняшнему дню на 7 дней
    week_ago = datetime.now() - timedelta(days=31)
    # Получаем все новости, опубликованные за последнюю неделю
    latest_news = News.objects.filter(date__gte=week_ago)
    return render(request, "landing/news.html", {"latest_news": latest_news})


def contacts(request):
    departments = Department.objects.all()
    return render(request, "landing/contacts.html", {"departments": departments})


def structure(request):
    departments = Department.objects.all()
    return render(request, "landing/structure.html", {"departments": departments})


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, "landing/department_detail.html", {"department": department})


def partners_view(request):
    partners = Partner.objects.all()
    return render(request, "landing/partners.html", {"partners": partners})


def contacts_admission(request):
    return render(request, "landing/contacts_admission.html")
