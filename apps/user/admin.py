import json

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.common.models import Country
from .models import User, Driver, Color

admin.site.unregister(Group)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "object_repr", "action_time")
    readonly_fields = (
        "id", "user", "content_type",
        "object_id", "object_repr",
        "action_flag", "change_message",
        "action_time"
    )


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["id", "username", "nickname", "telegram_id", "phone_number", "is_driver"]
    list_display_links = ["id", "username"]
    readonly_fields = ["id", "last_login", "date_joined"]
    search_fields = ["username"]
    actions = ["load_uzb_regions"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("full_name", "nickname", "email", "phone_number")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_driver",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    def load_uzb_regions(self, request, queryset=None):
        Country.objects.all().delete()
        with open("data/uzbekistan_regions.json", "r", encoding="utf-8") as f:
            regions_data = json.load(f)

        regions = []
        districts = []

        # Viloyatlarni yig'ish
        for region in regions_data:
            regions.append(Country(name=region["name"], parent=None))

        # Bulk create viloyatlar
        regions = Country.objects.bulk_create(regions)

        # Tumanlarni yig'ish
        for region, region_obj in zip(regions_data, regions):
            for district in region["districts"]:
                districts.append(Country(name=district, parent=region_obj))

        # Bulk create tumanlar
        Country.objects.bulk_create(districts)

        print("✅ Barcha viloyatlar va tumanlar yuklandi!")


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


admin.site.register(Color)
