from rest_framework_mongoengine import serializers

from backend.core.models import Event, Author
from backend.core.serializers import AuthorSerializer


class EventSerializer(serializers.DocumentSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        ref_name = "Event"
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        event = Event.objects.create(**validated_data)
        event.authors = []

        for author_data in authors_data:
            event.authors.append(Author(**author_data))

        event.save()
        return event

    def update(self, instance, validated_data):
        authors_data = validated_data.pop("authors")
        event = super(EventSerializer, self).update(instance, validated_data)

        for author_data in authors_data:
            event.authors.append(Author(**author_data))

        event.save()
        return event
