from mongoengine import Document, fields

from backend.core.models import Event


class Submission(Document):
    title = fields.StringField(max_length=50)
    title_english = fields.StringField(max_length=50)
    file = fields.FileField(required=True)
    created_at = fields.StringField(max_length=19)
    event_ref = fields.ReferenceField(Event, required=True)
    authors = fields.ListField(required=True)
