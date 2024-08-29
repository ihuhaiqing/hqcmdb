from django.contrib import admin
from application.models import MySQL

@admin.register(MySQL)
class MySQLAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port', 'user', 'get_plain_password', 'database')
    search_fields = ('name', 'host__hostname', 'database')
    list_filter = ('host',)

    def get_plain_password(self, obj):
        return obj.password
    get_plain_password.short_description = '明文密码'
