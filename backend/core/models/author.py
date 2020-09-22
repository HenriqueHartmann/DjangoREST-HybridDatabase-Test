from rest_framework_mongoengine import EmbeddedDocument, fields


class Author(EmbeddedDocument):
    id = fields.IntField()
