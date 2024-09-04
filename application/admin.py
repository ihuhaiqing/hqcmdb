from django import forms
from django.contrib import admin
from application.models import MySQL

@admin.register(MySQL)
class MySQLAdmin(admin.ModelAdmin):
    list_display = ('database_name', 'project', 'host', 'port', 'role', 'username', 'password', 'version', 'environment', 'created_at', 'updated_at')
    search_fields = ('host__ip_address',)
    list_filter = ('database_name', 'project', 'environment')
    change_form_template = 'admin/application/change_form.html'
