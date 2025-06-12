from django.contrib import admin
from .models import Order, OrderedItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "phone",
        "address",
        "city",
        "state",
        "date_of_order",
        "completed",
    )
    list_display_links = ("customer",)


@admin.register(OrderedItem)
class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "order", "quantity", "date_added")
    list_display_links = ("book",)
