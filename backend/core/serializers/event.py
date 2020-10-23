from rest_framework_mongoengine import serializers

from backend.core.models import Event


class EventSerializer(serializers.DocumentSerializer):
    class Meta:
        ref_name = "Event"
        model = Event
        fields = "__all__"
