from django.db import models
from colorfield.fields import ColorField
from apps.user.models import User


class Vehicle(models.Model):
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
    plate_number = models.CharField(max_length=20, verbose_name="Plate Number", null=True, blank=True)
    make = models.CharField(max_length=50, verbose_name="Brand")
    model = models.CharField(max_length=50, verbose_name="Model")
    year = models.IntegerField()
    color = ColorField(default='#FFFFFF', choices=COLOR_PALETTE)
    image = models.ImageField(upload_to="vehicle/")

    class Meta:
        db_table = "vehicles"
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.plate_number


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field="telegram_id")
    license_number = models.CharField(max_length=20)
    license_expiry_date = models.DateField(null=True, blank=True)
    license_image = models.ImageField(upload_to="driver/license/")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name="drivers")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "drivers"
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return self.user.get_full_name()
