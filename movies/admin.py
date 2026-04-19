from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "release_date", "is_active")
    list_filter = ("is_active", "genre", "release_date")
    search_fields = ("title", "synopsis")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")