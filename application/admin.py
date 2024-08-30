from django.contrib import admin
from application.models import MySQL
# from utils.cryptography import decrypt_data

@admin.register(MySQL)
class MySQLAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'username', 'password', 'database_name', 'version', 'created_at', 'updated_at')
    search_fields = ('host__hostname', 'database_name', 'version')
    list_filter = ('host', 'version')
