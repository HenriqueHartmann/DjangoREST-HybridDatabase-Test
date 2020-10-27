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

    def list(self, request):
        queryset = models.User.objects.all()
        serializer = serializers.UserShowSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = models.User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UserShowSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        users = models.User.objects.all()
        user = get_object_or_404(users, pk=pk)
        first_name = user.profile["first_name"]
        last_name = user.profile["last_name"]
        date_now = datetime.now().strftime("%d-%m-%YT%H:%M:%S")

        request.data["email"] = user.email
        request.data["profile"]["password"] = user.profile["password"]
        request.data["created_at"] = user.created_at

        data_record = {}
        data_record["records"] = []
        data_record["records"].append({})
        data_record["id_user"] = pk
        data_record["records"][0]["first_name"] = first_name
        data_record["records"][0]["last_name"] = last_name
        data_record["records"][0]["updated_at"] = date_now

        data = {}

        # UPDATE
        records = models.UserRecord.objects.all()
        for record in records:
            if pk == record.id_user:
                serializer_user = serializers.UserSerializer(user, data=request.data)
                serializer_record = serializers.UserRecordSerializer(record, data=data_record)
                if serializer_user.is_valid():
                    if serialize_record.is_valid():
                        serializer_user.save()
                        serializer_record.save()
                        data["user"] = serializer_user.data
                        data["record"] = serializer_record.data
                        return Response(data, status=status.HTTP_200_OK)
                    return Response(serializer_record.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)

        # CREATE
        serializer_user = serializers.UserSerializer(user, data=request.data)
        serializer_record = serializers.UserRecordSerializer(data=data_record)
        if serializer_user.is_valid():
            if serializer_record.is_valid():
                serializer_user.save()
                serializer_record.save()
                data["user"] = serializer_user.data
                data["record"] = serializer_record.data
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer_record.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=True, url_path="get-password")
    def retrieve_password(self, request, pk=None):
        queryset = models.User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="record")
    def list_records(self, request):
        if models.User.objects.count() > 0:
            list_all = []
            users = models.User.objects.all()
            for user in users:
                list_temp = {}
                list_temp["user"] = user
                if models.UserRecord.objects.count() > 0:
                    records = models.UserRecord.objects.all()
                    for record in records:
                        if int(record.id_user) == user.id:
                            list_temp["record"] = record
                list_all.append(list_temp)
            serializer = serializers.ListUserRecordsSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path="record")
    def retrieve_records(self, request, pk=None):
        users = models.User.objects.all()
        user = get_object_or_404(users, pk=pk)
        list_records = {}

        list_records["user"] = user
        if models.UserRecord.objects.count() > 0:
            records = models.UserRecord.objects.all()
            for record in records:
                if int(record.id_user) == user.id:
                    list_records["record"] = record
        serializer = serializers.ListUserRecordsSerializer(list_records)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="event")
    def list_users_events(self, request):
        if models.User.objects.count() > 0:
            list_all = []
            users = models.User.objects.all()
            for user in users:
                list_temp = {}
                list_temp["user"] = user
                if models.Event.objects.count() > 0:
                    events = models.Event.objects.all()
                    list_temp["events"] = []
                    for event in events:
                        list_ids = [int(a) for a in event.authors]
                        if user.id in list_ids:
                            list_temp["events"].append(event)
                list_all.append(list_temp)
            serializer = serializers.ListEventsSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path="event")
    def list_user_events(self, request, pk=None):
        users = models.User.objects.all()
        user = get_object_or_404(users, pk=pk)
        list_user_events = {}
        list_user_events["user"] = user

        if models.Event.objects.count() > 0:
            events = models.Event.objects.all()
            list_user_events["events"] = []
            for event in events:
                list_ids = [int(a) for a in event.authors]
                if user.id in list_ids:
                    list_user_events["events"].append(event)
        serializer = serializers.ListEventsSerializer(list_user_events)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="submission")
    def list_user_submission(self, request):
        if models.User.objects.count() > 0:
            list_all = []
            users = models.User.objects.all()
            for user in users:
                list_temp = {}
                list_temp["user"] = user
                if models.Submission.objects.count() > 0:
                    submissions = models.Submission.objects.all()
                    list_temp["submissions"] = []
                    for submission in submissions:
                        list_ids = [int(a) for a in submission.authors]
                        if user.id in list_ids:
                            list_temp["submissions"].append(submission)
                list_all.append(list_temp)
            serializer = serializers.ListSubmissionsSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path="submission")
    def list_user_submissions(self, request, pk=None):
        users = models.User.objects.all()
        user = get_object_or_404(users, pk=pk)
        list_user_submissions = {}
        list_user_submissions["user"] = user

        if models.Submission.objects.count() > 0:
            submissions = models.Submission.objects.all()
            list_user_submissions["submissions"] = []
            for submission in submissions:
                list_ids = [int(a) for a in submission.authors]
                if user.id in list_ids:
                    list_user_submissions["submissions"].append(submission)
        serializer = serializers.ListSubmissionsSerializer(list_user_submissions)
        return Response(serializer.data, status=status.HTTP_200_OK)
