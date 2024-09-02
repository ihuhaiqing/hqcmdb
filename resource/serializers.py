from rest_framework import serializers
from .models import Host

class HostSerializer(serializers.ModelSerializer):
    targets = serializers.SerializerMethodField()
    labels = serializers.SerializerMethodField()

    class Meta:
        model = Host
        fields = ['targets', "labels"]

    def get_targets(self, obj):
        return [obj.ip_address + ":9100"]
    
    def get_labels(self, obj):
        return {"hostname": obj.hostname, "description": obj.description}
