from rest_framework_mongoengine import serializers

from backend.core.models import Author


class AuthorSerializer(serializers.EmbeddedDocumentSerializer):
    ref_name = "AuthorEvent"
    model = Author
