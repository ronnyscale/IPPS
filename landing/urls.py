from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("news/", news, name="news"),
    path("contacts/", contacts, name="contacts"),
    path("structure/", structure, name="structure"),
    path("department/<int:pk>/", department_detail, name="department_detail"),
    path("partners/", partners_view, name="partners"),
    path("contactsadmin/", contacts_admission, name="contacts_admission"),
]
