from rest_framework import status, viewsets

from backend.core import models
from backend.core import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
