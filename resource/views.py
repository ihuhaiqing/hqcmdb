from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Host
from .serializers import HostSerializer

# for promethues host targets discovery
class HostTargetsViewSet(APIView):
    def get(self, request):
        items = Host.objects.all()
        serializer = HostSerializer(items, many=True)
        return Response(serializer.data)