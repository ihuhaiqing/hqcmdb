from django.contrib import admin
from common.models import OperatingSystem, Environment, Project

@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
    search_fields = ('name', 'version')

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'project_manager', 'created_at', 'updated_at')
    search_fields = ('name', 'project_manager')
    list_filter = ('status', )

