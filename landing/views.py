from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from core.models import News
from datetime import datetime, timedelta
from core.models import *

def index(request):
    # Получаем дату, предшествующую сегодняшнему дню на 30 дней
    week_ago = datetime.now() - timedelta(days=30)

    # Получаем все новости, опубликованные за последнюю неделю
    latest_news = News.objects.filter(date__gte=week_ago).order_by("-date")
    announcements = Announcement.objects.all().order_by("-created_at")

    # Пагинация для новостей
    news_paginator = Paginator(latest_news, 3)  # 3 новости на страницу
    news_page_number = request.GET.get("news_page")
    news_page_obj = news_paginator.get_page(news_page_number)

    # Пагинация для объявлений
    announcements_paginator = Paginator(announcements, 3)  # 3 объявления на страницу
    announcements_page_number = request.GET.get("announcements_page")
    announcements_page_obj = announcements_paginator.get_page(announcements_page_number)

    return render(
        request,
        "landing/index.html",
        {
            "news_page_obj": news_page_obj,
            "announcements_page_obj": announcements_page_obj,
        },
    )


def about(request):
    return render(request, "landing/about.html")


def news(request):
    # Получаем все новости
    all_news = News.objects.all()

    # Инициализируем Paginator, указывая количество новостей на странице (6)
    paginator = Paginator(all_news, 6)

    page_number = request.GET.get("page")
    try:
        # Получаем страницу
        latest_news = paginator.page(page_number)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, выводим первую страницу
        latest_news = paginator.page(1)
    except EmptyPage:
        # Если страница пуста, выводим последнюю страницу
        latest_news = paginator.page(paginator.num_pages)

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


def schedule_view(request, schedule_type):
    education_level = request.GET.get("level", "B")
    form = request.GET.get("form", "FT")
    course = request.GET.get("course")
    group = request.GET.get("group")

    filters = {
        "schedule_type": schedule_type,
        "education_level": education_level,
        "form": form,
    }

    if course:
        filters["course"] = course

    if group:
        filters["group"] = group

    schedules = Schedule.objects.filter(**filters) if course and group else []

    courses = (
        Schedule.objects.filter(
            schedule_type=schedule_type, education_level=education_level, form=form
        )
        .values_list("course", flat=True)
        .distinct()
    )

    groups = (
        Schedule.objects.filter(
            schedule_type=schedule_type,
            education_level=education_level,
            form=form,
            course=course,
        )
        .values_list("group", flat=True)
        .distinct()
        if course
        else []
    )

    context = {
        "schedules": schedules,
        "selected_level": education_level,
        "selected_form": form,
        "schedule_type": schedule_type,
        "courses": courses,
        "groups": groups,
        "selected_course": course,
        "selected_group": group,
    }

    return render(request, "landing/schedule.html", context)


def additional_education_programs(request):
    additional_education_programs = AdditionalEducationProgram.objects.all()
    return render(
        request,
        "landing/additional_programs.html",
        {"additional_education_programs": additional_education_programs},
    )
