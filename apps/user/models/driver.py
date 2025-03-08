from datetime import date

from django.db import models
from colorfield.fields import ColorField
from apps.user.models import User


class Color(models.Model):
    COLOR_PALETTE = [
        ('#FFFFFF', 'White'),
        ('#000000', 'Black'),
        ('#FF0000', 'Red'),
        ('#00FF00', 'Green'),
        ('#0000FF', 'Blue'),
        ('#FFFF00', 'Yellow'),
        ('#FF00FF', 'Magenta'),
        ('#00FFFF', 'Cyan'),
        ('#FFA500', 'Orange'),
    ]
    name = models.CharField(max_length=15, null=True)
    color = ColorField(default='#FFFFFF', choices=COLOR_PALETTE)

    class Meta:
        db_table = "colors"


class Driver(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        to_field="telegram_id",
    )
    experience = models.IntegerField(null=True, blank=True)
    license_number = models.CharField(max_length=20, null=True, blank=True)
    license_expiry_date = models.CharField(max_length=20, null=True, blank=True)
    license_image = models.ImageField(upload_to="drivers/licenses/", null=True, blank=True)
    plate_number = models.CharField(max_length=20, verbose_name="Plate Number", null=True, blank=True)
    model = models.CharField(max_length=50, verbose_name="Model", null=True)  # for example: Corolla, Camry, etc.
    year = models.IntegerField(default=date.today().year)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="vehicles", null=True)
    image = models.ImageField(upload_to="drivers/vehicle/", null=True, blank=True)

    class Meta:
        db_table = "drivers"

    def __str__(self):
        return self.user.get_full_name()
