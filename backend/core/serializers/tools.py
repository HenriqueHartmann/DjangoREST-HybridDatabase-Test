from rest_framework import serializers

from backend.core.serializers import EventSerializer, SubmissionSerializer, UserRecordSerializer


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

class ListUsersEventSerializer(serializers.Serializer):
    event = EventSerializer()
    users = UserShowSerializer(many=True)

class ListSubmissionsSerializer(serializers.Serializer):
    user = UserShowSerializer()
    submissions = SubmissionSerializer(required=False, many=True)

class ListUsersSubmissionsSerializer(serializers.Serializer):
    submission = SubmissionSerializer()
    users = UserShowSerializer(many=True)
