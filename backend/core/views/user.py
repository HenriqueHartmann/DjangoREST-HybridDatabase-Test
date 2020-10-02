from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(methods=["GET"], detail=False, url_path="event")
    def list_users_events(self, request):
        users = models.User.objects.all()
        events = models.Event.objects.all()

        list_temp = {}
        list_all = []

        if models.User.objects.count() > 0:
            for user in users:
                list_temp["user"] = user
                if models.Event.objects.count() > 0:
                    list_temp["events"] = []
                    for event in events:
                        list_ids = []
                        for author in event.authors:
                            list_ids.append(int(author.id_user))
                        if user.id in list_ids:
                            list_temp["events"].append(event)
                list_all.append(list_temp)
                list_temp = {}
            serializer = serializers.ListEventsSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path="event")
    def list_user_events(self, request, pk=None):
        users = models.User.objects.all()
        user = get_object_or_404(users, pk=pk)
        events = models.Event.objects.all()

        list_user_events = {}
        list_user_events["user"] = user

        if models.Event.objects.count() > 0:
            list_user_events["events"] = []
            for event in events:
                list_ids = []
                for author in event.authors:
                    list_ids.append(int(author.id_user))
                if user.id in list_ids:
                    list_user_events["events"].append(event)
        serializer = serializers.ListEventsSerializer(list_user_events)
        return Response(serializer.data, status=status.HTTP_200_OK)
