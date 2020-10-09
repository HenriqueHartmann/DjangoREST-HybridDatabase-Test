from rest_framework_mongoengine import serializers

from backend.core.models import UserRecord, DataUserRecord


class DataUserRecordSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        ref_name = "DataUserRecord"
        model = DataUserRecord


class UserRecordSerializer(serializers.DocumentSerializer):
    records = DataUserRecordSerializer(many=True)

    class Meta:
        ref_name = "UserRecord"
        model = UserRecord

    def create(self, validated_data):
        data_records = validated_data.pop("records")
        record = UserRecord.objects.create(**validated_data)
        record.records = []

        for data_record in data_records:
            record.records.append(DataUserRecord(**data_record))

        record.save()
        return record

    def update(self, instance, validated_data):
        data_records = validated_data.pop("records")
        record = super(UserRecordSerializer, self).update(instance, validated_data)

        for data_record in data_records:
            record.records.append(DataUserRecord(**data_record))

        record.save()
        return record
