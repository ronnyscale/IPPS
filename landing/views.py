from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from core.models import News
from datetime import datetime, timedelta
from core.models import *


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


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, "landing/news_detail.html", {"news_item": news_item})


def contacts(request):
    departments = Department.objects.all()
    return render(request, "landing/contacts.html", {"departments": departments})


def structure(request):
    departments = Department.objects.all()
    return render(request, "landing/structure.html", {"departments": departments})


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    members = department.members.all()
    return render(request, "landing/department_detail.html", {"department": department, "members": members})


def partners_view(request):
    partners = Partner.objects.all()
    return render(request, "landing/partners.html", {"partners": partners})


def contacts_admission(request):
    return render(request, "landing/contacts_admission.html")


def academic_council_list(request):
    academic_council_members = Person.objects.filter(council_members__isnull=False)
    return render(
        request,
        "landing/academic_council_list.html",
        {"academic_council_members": academic_council_members},
    )


def student_life_event_list(request):
    events = StudentLifeEvent.objects.all()
    return render(request, "landing/student_life_event_list.html", {"events": events})


def youth_centre(request):
    youth_divisions = YouthDivision.objects.all()
    return render(request, "landing/youth_centre.html", {"youth_divisions": youth_divisions})


def undergraduate_program(request):
    selected_level = request.GET.get("level", "B")
    specialties = Speciality.objects.filter(education_level=selected_level)

    # Ссылки для каждого уровня образования
    admission_rules_links = {
        "B": "https://admissions.sfu-kras.ru/exams",
        "M": "https://admissions.sfu-kras.ru/magisters",
        "P": "https://admissions.sfu-kras.ru/post-graduates",
    }
    admission_plan_links = {
        "B": "https://admissions.sfu-kras.ru/exams",
        "M": "https://admissions.sfu-kras.ru/magisters",
        "P": "https://admissions.sfu-kras.ru/post-graduates",
    }

    context = {
        "specialties": specialties,
        "selected_level": selected_level,
        "admission_rules_link": admission_rules_links[selected_level],
        "admission_plan_link": admission_plan_links[selected_level],
    }
    return render(request, "landing/undergraduate_program.html", context)


def specialty_detail(request, specialty_id):
    specialty = get_object_or_404(Speciality, id=specialty_id)
    return render(request, "landing/specialty_detail.html", {"specialty": specialty})


def project_list(request):
    # Получаем список всех годов, для которых есть проекты
    years = Project.objects.datetimes("date", "year")

    # Получаем год из GET-параметра, если он передан, иначе - текущий год
    selected_year = request.GET.get("year")
    if selected_year:
        projects = Project.objects.filter(date__year=selected_year)
    else:
        projects = Project.objects.filter(date__year=timezone.now().year)

    context = {
        "projects": projects,
        "years": years,
        "selected_year": selected_year,
    }
    return render(request, "landing/project_list.html", context)


def events(request):
    events = Event.objects.all()
    return render(request, "landing/events.html", {"events": events})


def supervisor_navigator(request):
    # Путь к PDF-файлу
    pdf_url = "/static/files/supervisor_navigator.pdf"
    return render(request, "landing/supervisor_navigator.html", {"pdf_url": pdf_url})
