from rest_framework_mongoengine import serializers

from backend.core.models import SubmissionRecord, DataSubmissionRecord


class DataSubmissionRecordSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        ref_name = "DataSubmissionRecord"
        model = DataSubmissionRecord


class SubmissionRecordSerializer(serializers.DocumentSerializer):
    records = DataSubmissionRecordSerializer(many=True)

    class Meta:
        ref_name = "SubmissionRecord"
        model = SubmissionRecord

    def create(self, validated_data):
        data_records = validated_data.pop("records")
        record = SubmissionRecord.objects.create(**validated_data)
        record.records = []

        for data_record in data_records:
            record.records.append(DataSubmissionRecord(**data_record))

        record.save()
        return record

    def update(self, instance, validated_data):
        data_records = validated_data.pop("records")
        record = super(SubmissionRecordSerializer, self).update(instance, validated_data)

        for data_record in data_records:
            record.records.append(DataSubmissionRecord(**data_record))

        record.save()
        return record
