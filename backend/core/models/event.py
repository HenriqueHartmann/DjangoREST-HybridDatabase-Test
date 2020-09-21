from mongoengine import Document, EmbeddedDocument, fields


class Author(EmbeddedDocument):
    id = fields.IntField()


class Event(Document):
    title = fields.StringField(max_length=50)
    title_english = fields.StringField(max_length=50)
    description = fields.StringField(max_length=255)
    starts_on = fields.StringField(max_length=19)
    ends_on = fields.StringField(max_length=19)
    authors = fields.EmbeddedDocumentListField(Author)
