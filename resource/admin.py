from django.contrib import admin
from common.mixin.export_excel import ExportExcelMixin
from .models import Host

# 注册主机模型
@admin.register(Host)
class HostAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ('hostname', 'ip_address', 'operating_system', 'project', 'environment', 'cpu_cores', 'memory_gb', 'storage_gb', 'description', 'password', 'created_at', 'updated_at')
    search_fields = ('ip_address',)
    list_filter = ('operating_system', 'environment')
    list_per_page = 14
    actions = ['export_as_excel']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(project__users=request.user)

