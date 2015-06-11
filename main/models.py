# coding: utf-8

import uuid

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    Simple 260 chars message stored by an user.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """ Uuid primary key """

    content = models.CharField(max_length=280, blank=False, null=False)
    """ Content of the little message """

    created_at = models.DateTimeField(auto_now_add=True)
    """ Creation Datetime of the message """

    user = models.ForeignKey(User, related_name='messages')
    """ User associated to the current message """