from mongoengine import EmbeddedDocument, fields


class Author(EmbeddedDocument):
    id = fields.IntField()
