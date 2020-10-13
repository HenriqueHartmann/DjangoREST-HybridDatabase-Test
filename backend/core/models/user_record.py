from mongoengine import Document, EmbeddedDocument, fields


class DataUserRecord(EmbeddedDocument):
    first_name = fields.StringField(max_length=25, required=True)
    last_name = fields.StringField(max_length=50, required=True)
    updated_at = fields.StringField(max_length=19)


class UserRecord(Document):
    user_id = fields.StringField(required=True)
    records = fields.EmbeddedDocumentListField(DataUserRecord)
