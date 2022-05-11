from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group, User
from django.forms import ModelForm

from .models import Entry


class EntryAdminForm(ModelForm):
    """Entry Form"""

    class Meta:
        model = Entry
        fields = ("pali", "sanskrit", "content")


class EntryAdmin(ModelAdmin):
    """Entry Admin"""

    form = EntryAdminForm
    add_form = EntryAdminForm

    list_display = ("pali", "sanskrit", "roman")
    search_fields = ("pali", "roman")


admin.site.register(Entry, EntryAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
