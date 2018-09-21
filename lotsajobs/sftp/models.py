import uuid

from django.db import models

class Request(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f'Request object ({self.uuid})'
