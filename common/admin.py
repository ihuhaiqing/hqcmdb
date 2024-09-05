from django.contrib import admin
from common.models import OperatingSystem, Environment, Project
from django.contrib.auth.models import User

from django.contrib import admin
from django.template.response import TemplateResponse

# 定义菜单顺序
def custom_index(request, extra_context=None):
    app_list = admin.site.get_app_list(request)
    # 定义应用的顺序
    order = ['resource', 'application', 'common', 'auth']
    app_list.sort(key=lambda x: order.index(x['app_label']) if x['app_label'] in order else len(order))
    context = dict(
        admin.site.each_context(request),
        title=admin.site.index_title,
        app_list=app_list,
    )
    return TemplateResponse(request, 'admin/index.html', context)
admin.site.index = custom_index

@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
    search_fields = ('name', 'version')

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'project_manager', 'display_users', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('status', )
    filter_horizontal = ['users']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user)

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    display_users.short_description = '项目成员'
