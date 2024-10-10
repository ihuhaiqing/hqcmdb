from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Host
from .serializers import HostSerializer

class HostTargetsViewSet(APIView):
    def get_queryset(self):
        return Host.objects.all()

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = HostSerializer(queryset, many=True)
        return Response(serializer.data)
