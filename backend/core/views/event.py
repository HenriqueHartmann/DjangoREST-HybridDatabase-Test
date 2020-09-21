from rest_framework_mongoengine import viewsets

from backend.core.models import Event
from backend.core.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
