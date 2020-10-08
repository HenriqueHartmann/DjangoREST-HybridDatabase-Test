from mongoengine import EmbeddedDocument, fields


class Author(EmbeddedDocument):
    id_user = fields.StringField(required=True)
