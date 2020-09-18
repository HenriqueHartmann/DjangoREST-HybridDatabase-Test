from rest_framework import serializers
from backend.core.models import User


class FieldProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=25)


class UserSerializer(serializers.ModelSerializer):
    profile = FieldProfileSerializer()

    class Meta:
        ref_name = "User"
        model = User
        fields = "__all__"
