from mongoengine import Document, fields


from backend.core.models import Author


class Submission(Document):
    title = fields.StringField(max_length=50)
    title_english = fields.StringField(max_length=50)
    file = fields.FileField(required=True)
    starts_on = fields.StringField(max_length=19)
    ends_on = fields.StringField(max_length=19)
    created_at = fields.StringField(max_length=19)
    event_ref = fields.StringField(required=True)
    authors = fields.EmbeddedDocumentListField(Author)
