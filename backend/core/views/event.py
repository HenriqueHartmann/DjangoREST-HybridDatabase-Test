from django.shortcuts import get_object_or_404
from rest_framework_mongoengine import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime

from backend.core import models
from backend.core import serializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def create(self, request):
        date = datetime.now()
        request.data["created_at"] = date.strftime("%d-%m-%YT%H:%M:%S")
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=False, url_path="user")
    def list_events_users(self, request):
        events = models.Event.objects.all()
        users = models.User.objects.all()
        list_all = []

        if models.Event.objects.count() > 0:
            for event in events:
                list_temp = {}
                list_temp["event"] = event
                if models.User.objects.count() > 0:
                    list_temp["users"] = []
                    for user in users:
                        list_ids = [int(a) for a in event.authors]
                        if user.id in list_ids:
                            list_temp["users"].append(user)
                list_all.append(list_temp)
            serializer = serializers.ListUsersSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)
    
    @action(methods=["GET"], detail=True, url_path="user")
    def list_event_users(self, request, id=None):
        events = models.Event.objects.all()
        event = get_object_or_404(events, id=id)
        users = models.User.objects.all()
        list_event_users = {}
        list_event_users["event"] = event

        if models.User.objects.count() > 0:
            list_event_users["users"] = []
            for user in users:
                list_ids = [int(a) for a in event.authors]
                if user.id in list_ids:
                    list_event_users["users"].append(user)
        serializer = serializers.ListUsersSerializer(list_event_users)
        return Response(serializer.data, status=status.HTTP_200_OK)
