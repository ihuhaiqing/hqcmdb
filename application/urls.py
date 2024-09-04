from django.urls import path

from application.views import get_hosts

urlpatterns = [
    path('hosts/<int:environment_id>/', get_hosts, name='get_hosts'),
]
