from rest_framework_mongoengine import serializers


class AuthorSerializer(serializers.EmbeddedDocumentSerializer):
    ref_name = "AuthorEvent"
    model = Author
