from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(verbose_name="password", max_length=128, null=True)
    nickname = models.CharField(max_length=255, null=True)
    telegram_id = models.BigIntegerField(unique=True, db_index=True)
    email = models.EmailField(null=True, blank=True)
    language_code = models.CharField(max_length=2, default="uz")
    phone_number = models.CharField(
        max_length=20,
        db_index=True,
        unique=True,
        blank=True,
        null=True,
    )
    district = models.ForeignKey(
        "common.Country",
        on_delete=models.SET_NULL,
        related_name="users",
        blank=True,
        null=True,
    )
    birth_year = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_driver = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["telegram_id"]

    class Meta:
        db_table = "users"
        ordering = ["-id"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"

    def age(self):
        return date.today().year - self.birth_year
