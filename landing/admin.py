from django.contrib import admin
from core.models import News, Project, Event, Department, Partner


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