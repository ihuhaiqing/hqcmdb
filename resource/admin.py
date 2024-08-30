from django import forms
from django.contrib import admin
from .models import Host

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'
        widgets = {
            'projects': forms.CheckboxSelectMultiple,  # 使用复选框显示多对多字段
        }

# 注册主机模型
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'operating_system', 'display_projects', 'environment', 'cpu_cores', 'memory_gb', 'storage_gb', 'description', 'password', 'created_at', 'updated_at')
    search_fields = ('ip_address',)
    list_filter = ('operating_system', 'environment')
    list_per_page = 20
    form = HostForm

    def display_projects(self, obj):
        return ", ".join([project.name for project in obj.projects.all()])
    display_projects.short_description = '项目'
