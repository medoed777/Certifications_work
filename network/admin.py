from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import NetworkNode, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "country", "city")


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "level",
        "city",
        "supplier",
        "debt_to_supplier",
        "created_at",
    ]
    list_filter = ["city", "country", "level"]

    actions = ["clear_debt"]

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="{}">{}</a>',
                reverse("admin:network_networknode_change", args=[obj.supplier.id]),
                obj.supplier.name,
            )
        return "-"

    supplier_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
