from django.contrib import admin
from .models import Host

# 注册主机模型
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'operating_system', 'cpu_cores', 'memory_gb', 'storage_gb', 'description', 'created_at', 'updated_at')
    search_fields = ('hostname', 'ip_address', 'operating_system')
    list_filter = ('operating_system', 'cpu_cores')
    list_per_page = 20

# 也可以使用简单的注册方式
# admin.site.register(Host, HostAdmin)

