from rest_framework_mongoengine import serializers

from backend.core.models import Submission, Author
from backend.core.serializers import AuthorSerializer


class SubmissionSerializer(serializers.DocumentSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        ref_name = "Submission"
        model = Submission
        fields = "__all__"

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        submission = Submission.objects.create(**validated_data)
        submission.authors = []

        for author_data in authors_data:
            submission.authors.append(Author(**author_data))

        submission.save()
        return submission

    def update(self, instance, validated_data):
        authors_data = validated_data.pop("authors")
        submission = super(SubmissionSerializer, self).update(instance, validated_data)

        for author_data in authors_data:
            submission.authors.append(Author(**author_data))

        submission.save()
        return submission
