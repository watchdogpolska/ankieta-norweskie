# coding=utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ThemesConfig(AppConfig):
    name = 'petycja_norweskie.themes'
    verbose_name = _("Themes")
