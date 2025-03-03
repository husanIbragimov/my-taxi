from django.db import models

from apps.common.models import BaseModel


class Group(BaseModel):
    group_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    district = models.ForeignKey("common.Country", on_delete=models.SET_NULL, null=True, blank=True, related_name="groups")
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    invite_link = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    who_added = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="added_groups")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "tg_groups"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.title}"


class Channel(BaseModel):
    channel_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    invite_link = models.CharField(max_length=255, null=True, blank=True)
    is_ad = models.BooleanField(default=False)

    class Meta:
        db_table = "channels"
        ordering = ["-id"]
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return f"{self.title}"
