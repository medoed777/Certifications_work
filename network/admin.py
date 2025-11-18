from django.contrib import admin

from network.models import Supplier, NetworkNode


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "city", "supplier", "debt_to_supplier", "created_at"]
    list_filter = ["city", "country", "level"]

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
