from django.http import QueryDict
from rest_framework_mongoengine import viewsets
from rest_framework import parsers, status
from rest_framework.response import Response
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

        data = json.loads(result.data["data"])
        
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Submission.objects.all()
    parser_classes = (MultipartJsonParser, parsers.JSONParser)
    serializer_class = serializers.SubmissionSerializer
        
    # Multipart field
    def create(self, request):
        date = datetime.now()
        request.data["created_at"] = date.strftime("%d-%m-%YT%H:%M:%S")
        sr = serializers.Test(data=request.data["authors"])
        if sr.is_valid():
            print(sr.data)
        else:
            print(sr.errors)
        print(request.data)
        serializer = serializers.SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
