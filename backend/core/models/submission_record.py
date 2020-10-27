from mongoengine import Document, EmbeddedDocument, fields


class DataSubmissionRecord(EmbeddedDocument):
    file = fields.FileField(required=True)
    upload_at = fields.StringField(max_length=19)


class SubmissionRecord(Document):
    id_user = fields.StringField(required=True)
    records = fields.EmbeddedDocumentListField(DataSubmissionRecord)
