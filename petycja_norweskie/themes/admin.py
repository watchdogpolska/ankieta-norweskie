# coding=utf-8
from django.contrib import admin

from petycja_norweskie.themes.models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'authorship', 'prefix')
    readonly_fields = ('prefix',)
