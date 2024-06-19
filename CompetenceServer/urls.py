from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home_view, name="home"),
    path("disciplines/", disciplines, name="disciplines"),
    path("competencies/", competencies, name="competencies"),
    path(
        "discipline/<slug:slug>/",
        discipline_detail_view,
        name="discipline_detail",
    ),
    path(
        "competencies/<slug:slug>/",
        competency_detail_view,
        name="competency_detail",
    ),
    path("search/", search_view, name="search"),
]
