from uuid import uuid4
from django.db import models
from django.utils.crypto import get_random_string
from main.utils.config import config


class API(models.Model):
    """
        API model
    """
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    key = models.CharField(max_length=255,  unique=True, default=get_random_string(length=36))
    prefix = models.CharField(max_length=255,  blank=False, default='api')
    version = models.CharField(max_length=255,  blank=False)
    system = models.CharField(max_length=255,  blank=False)
    module = models.CharField(max_length=255,  blank=False)
    actor = models.CharField(max_length=255,  blank=False)
    function = models.CharField(max_length=255,  blank=False)

    class Meta:
        db_table = "api"