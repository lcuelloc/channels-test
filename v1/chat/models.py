from django.db import models

from v1.utils.models.core import CoreModel


class Chat(CoreModel):
    """
    Message model.

    Simple save string message
    """

    message = models.TextField(max_length=5000)

    class Meta:
        ordering = ['-id']
        get_latest_by = 'created'

    def __str__(self):
        return '{}'.format(self.pk)
