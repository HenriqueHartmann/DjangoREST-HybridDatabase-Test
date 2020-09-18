from django.db import models
from django.contrib.postgres.fields import JSONField


class User(models.Model):
    profile = JSONField()
    email = models.EmailField(unique=True)
    created_at = models.CharField()

    def __str__():
        return self.name
