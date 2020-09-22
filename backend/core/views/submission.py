from rest_framework_mongoengine import viewsets

from backend.core.models import Submission
from backend.core.serializers import SubmissionSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
