from django.db import models
from uuid import uuid4


class Account(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_time=models.DateTimeField(auto_now_add=True, editable=False)
    name=models.CharField(max_length=255, blank=False)
    password=models.CharField(max_length=255, blank=False)

    class Meta:
        db_table="account"
