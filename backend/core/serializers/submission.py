from rest_framework_mongoengine import serializers

from backend.core.models import Submission


class SubmissionSerializer(serializers.DocumentSerializer):
    class Meta:
        ref_name = "Submission"
        model = Submission
        fields = "__all__"
