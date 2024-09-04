from django.http import JsonResponse
from resource.models import Host

def get_hosts(request, environment_id):
    hosts = Host.objects.filter(environment_id=environment_id).values('id', 'ip_address')
    return JsonResponse(list(hosts), safe=False)
