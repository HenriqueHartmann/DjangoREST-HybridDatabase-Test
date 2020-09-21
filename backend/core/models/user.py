from django.db import models
from django.db.models import JSONField


class User(models.Model):
    profile = JSONField()
    email = models.EmailField(unique=True)
    created_at = models.CharField(max_length=19)

    def __str__():
        return self.name
