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
    color = ColorField(default='#FFFFFF', choices=COLOR_PALETTE)

    class Meta:
        db_table = "colors"


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, verbose_name="Plate Number", null=True, blank=True)
    make = models.CharField(max_length=50, verbose_name="Brand")  # for example: Toyota, Honda, etc.
    model = models.CharField(max_length=50, verbose_name="Model")  # for example: Corolla, Camry, etc.
    year = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="vehicles", null=True)
    image = models.ImageField(upload_to="vehicle/")

    class Meta:
        db_table = "vehicles"
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.plate_number


class Driver(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        to_field="telegram_id",
        primary_key=True,
    )
    experience = models.IntegerField(null=True, blank=True)
    license_number = models.CharField(max_length=20)
    license_expiry_date = models.DateField(null=True, blank=True)
    license_image = models.ImageField(upload_to="driver/license/")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT, related_name="drivers")

    class Meta:
        db_table = "drivers"

    def __str__(self):
        return self.user.get_full_name()
