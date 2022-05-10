from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group, User

from .models import Entry


class EntryAdmin(ModelAdmin):
    """Entry Admin"""

    list_display = ("pali", "grammar")
    search_fields = ("pali", "roman")


admin.site.register(Entry, EntryAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
