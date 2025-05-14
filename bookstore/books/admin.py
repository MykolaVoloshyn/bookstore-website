from django.contrib import admin
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "genre",
        "publisher",
        "price",
        "in_stock",
        "new",
        "on_sale",
    )
    list_display_links = ("title",)
    list_editable = ("in_stock", "new")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "author", "publisher")


admin.site.register(Author)
admin.site.register(Publisher)
