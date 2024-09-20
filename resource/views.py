from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Host
from .serializers import HostSerializer
from rest_framework.permissions import IsAuthenticated

# for promethues host targets discovery
class HostTargetsViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        items = Host.objects.all()
        serializer = HostSerializer(items, many=True)
        return Response(serializer.data)