from rest_framework_mongoengine import viewsets

from backend.core.models import UserRecord
from backend.core.serializers import UserRecordSerializer


class UserRecordViewSet(viewsets.ModelViewSet):
    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer
