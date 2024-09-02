from django.urls import path
from .views import HostTargetsViewSet

urlpatterns = [
    path('host/targets/', HostTargetsViewSet.as_view(), name='host_targets'),
]
