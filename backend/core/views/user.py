from rest_framework import status, viewsets
from rest_framework.response import Response
from datetime import datetime

from backend.core import models
from backend.core import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request):
        date = datetime.now()
        request.data["created_at"] = date.strftime("%d-%m-%YT%H:%M:%S")
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
