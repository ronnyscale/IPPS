from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("news/", news, name="news"),
    path("news/<slug:slug>/", news_detail, name="news_detail"),
    # контакты
    path("contacts/", contacts, name="contacts"),
    path("contactsadmin/", contacts_admission, name="contacts_admission"),
    # ученый совет
    path("academic-council/", academic_council_list, name="academic_council_list"),
    # структура иппс
    path("structure/", structure, name="structure"),
    path("department/<int:pk>/", department_detail, name="department_detail"),
    path("partners/", partners_view, name="partners"),
    path("student-life-events/", student_life_event_list, name="student_event_list"),
    path("youth-centre/", youth_centre, name="youth_centre"),
    path("undergraduate/", undergraduate_program, name="undergraduate_program"),
    path("specialty/<int:specialty_id>/", specialty_detail, name="specialty_detail"),
    path("project-list/", project_list, name="project_list"),
    path("events/", events, name="events"),
    path(
        "supervisor-navigator/", supervisor_navigator, name="supervisor_navigator"
    ),
]
