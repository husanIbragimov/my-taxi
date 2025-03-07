from ckeditor.fields import RichTextField
from django.db import models

from apps.common.models import BaseModel


class KeyWord(models.Model):
    word = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "keywords"


class StatusChoice(models.IntegerChoices):
    NEW = 0, "New"
    IN_PROGRESS = 1, "In progress"
    DONE = 2, "Done"
    CANCELED = 3, "Canceled"


class Order(BaseModel):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        to_field="telegram_id",
        related_name="orders"
    )
    driver = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        null=True, blank=True,
        to_field="telegram_id",
        related_name="driver_orders"
    )
    # location or address
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    district = models.ForeignKey(
        "common.Country",
        on_delete=models.CASCADE,
        null=True, blank=True,
        limit_choices_to={"parent__isnull": False},
        related_name="orders"
    )
    address = models.TextField(null=True, blank=True)

    from_where = models.CharField(max_length=255, null=True, blank=True)
    to_where = models.CharField(max_length=255, null=True, blank=True)

    content = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # 10 000 000.00
    when = models.CharField(max_length=15, null=True, blank=True)

    status = models.IntegerField(
        choices=StatusChoice.choices,
        default=StatusChoice.NEW,
        db_index=True
    )
    # if status is canceled, then this field must be filled
    reason = models.CharField(max_length=255, null=True, blank=True)

    # if user wants to use service, then this field must be filled
    use_service = models.BooleanField(default=False)
    checked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "orders"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}"
