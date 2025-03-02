import json
from django.contrib import admin

from apps.common.models import Country
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "telegram_id"]
    readonly_fields = ["id", "last_login", "date_joined"]
    actions = ["load_uzb_regions"]

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
