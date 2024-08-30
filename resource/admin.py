from django.contrib import admin
from .models import Host

# 注册主机模型
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'operating_system', 'display_projects', 'environment', 'cpu_cores', 'memory_gb', 'storage_gb', 'description', 'password', 'created_at', 'updated_at')
    search_fields = ('ip_address',)
    list_filter = ('operating_system', 'environment')
    list_per_page = 20

    def display_projects(self, obj):
        return ", ".join([project.name for project in obj.projects.all()])
    display_projects.short_description = '项目'

# 也可以使用简单的注册方式
# admin.site.register(Host, HostAdmin)

