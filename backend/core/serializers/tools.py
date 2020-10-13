from rest_framework import serializers

from backend.core.serializers import EventSerializer, UserRecordSerializer


class FieldProfileShowSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=50)

class UserShowSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile = FieldProfileShowSerializer()
    email = serializers.EmailField()
    created_at = serializers.CharField()

class ListUserRecordsSerializer(serializers.Serializer):
    user = UserShowSerializer()
    record = UserRecordSerializer(required=False)

class ListEventsSerializer(serializers.Serializer):
    user = UserShowSerializer()
    events = EventSerializer(required=False, many=True)

class ListUsersSerializer(serializers.Serializer):
    event = EventSerializer()
    users = UserShowSerializer(many=True)
