from django.contrib import admin

from apps.order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "driver", "status"]
    list_display_links = ["id", "user"]
    readonly_fields = [
        "user", "driver",
        "status", "content",
        "address", "district",
        "to_where", "from_where",
        "checked_at", "use_service",
        "longitude", "latitude", "when",
        "reason", "created_at", "updated_at",
        "json_data"
    ]
    search_fields = ["user__username", "driver__username"]
    actions = ["change_status_to_done"]

    def change_status_to_done(self, request, queryset=None):
        queryset.update(status=2)
        self.message_user(request, "Status of selected orders changed to Done")
