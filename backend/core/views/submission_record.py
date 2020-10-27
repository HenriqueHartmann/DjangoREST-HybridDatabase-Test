from rest_framework_mongoengine import viewsets

from backend.core.models import SubmissionRecord
from backend.core.serializers import SubmissionRecordSerializer


class SubmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = SubmissionRecord.objects.all()
    serializer_class = SubmissionRecordSerializer
