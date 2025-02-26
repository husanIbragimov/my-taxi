from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = None
    telegram_id = models.CharField(max_length=20, db_index=True, unique=True)
    phone_number = models.CharField(
        max_length=20,
        db_index=True,
        unique=True,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_driver = models.BooleanField(default=False)

    class Meta:
        db_table = "users"
        ordering = ["-id"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"
