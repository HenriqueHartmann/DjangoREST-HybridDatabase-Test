from rest_framework import serializers

from backend.core.serializers import UserSerializer, EventSerializer


class ListEventsSerializer(serializers.Serializer):
    user = UserSerializer()
    events = EventSerializer(required=False, many=True)
