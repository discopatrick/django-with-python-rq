from django.db import models


class SftpJob(models.Model):
    uuid = models.UUIDField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'SftpJob object ({self.id}, {self.uuid})'
