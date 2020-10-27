from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework_mongoengine import viewsets
from rest_framework import parsers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import parser_classes
from datetime import datetime
import json

from backend.core import models
from backend.core import serializers


class MultipartJsonParser(parsers.MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}

        for key, value in result.data.items():
            if type(value) != str:
                data[key] = value
                continue
            if '{' in value or "[" in value:
                try:
                    data[key] = json.loads(value)
                except ValueError:
                    data[key] = value
            else:
                data[key] = value
    
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Submission.objects.all()
    parser_classes = (MultipartJsonParser, parsers.JSONParser)
    serializer_class = serializers.SubmissionSerializer

    def create(self, request):
        date = datetime.now()
        request.data["created_at"] = date.strftime("%d-%m-%YT%H:%M:%S")
        serializer = serializers.SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=False, url_path="user")
    def list_submissions_users(self, request):
        submissions = models.Submission.objects.all()
        users = models.User.objects.all()
        list_all = []

        if models.Submission.objects.count() > 0:
            for submission in submissions:
                list_temp = {}
                list_temp["submission"] = submission
                if models.User.objects.count() > 0:
                    list_temp["users"] = []
                    for user in users:
                        list_ids = [int(a) for a in submission.authors]
                        if user.id in list_ids:
                            list_temp["users"].append(user)
                list_all.append(list_temp)
            serializer = serializers.ListUsersSubmissionsSerializer(list_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path="user")
    def list_submission_users(self, request, id=None):
        submissions = models.Submission.objects.all()
        submission = get_object_or_404(submissions, id=id)
        users = models.User.objects.all()
        list_submission_users = {}
        list_submission_users["submission"] = submission

        if models.User.objects.count() > 0:
            list_submission_users["users"] = []
            for user in users:
                list_ids = [int(a) for a in submission.authors]
                if user.id in list_ids:
                    list_submission_users["users"].append(user)
        serializer = serializers.ListUsersSubmissionsSerializer(list_submission_users)
        return Response(serializer.data, status=status.HTTP_200_OK)
