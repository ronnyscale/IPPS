from django.contrib import admin
from core.models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title', 'content']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ['name', 'description']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ['name', 'description']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ['name', 'url']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ["first_name", "last_name", "email"]


@admin.register(AcademicCouncil)
class AcademicCouncilAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(AcademicTitle)
class AcademicTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(StudentLifeEvent)
class StudentLifeEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ['name', 'description']


@admin.register(YouthDivision)
class YouthDivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'activities')
    search_fields = ["name", "activities"]


@admin.register(Speciality)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "career")
    search_fields = ["name", "career"]


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]
