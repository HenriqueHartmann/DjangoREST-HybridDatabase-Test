from mongoengine import Document, EmbeddedDocument, fields


from backend.core.models import Author


class Submission(Document):
    title = fields.StringField(max_length=50)
    title_english = fields.StringField(max_length=50)
    file = fields.FileField()
    starts_on = fields.StringField(max_length=19)
    ends_on = fields.StringField(max_length=19)
    authors = fields.EmbeddedDocumentListField(Author)
