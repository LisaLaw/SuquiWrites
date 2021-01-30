from django.contrib import admin
from suquiwrites.models import Entry, Comment


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]
    list_filter = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "text", "date_posted", "connected_entry"]
    readonly_fields = ["connected_entry"]
    list_filter = ["name", "date_posted", "connected_entry"]
