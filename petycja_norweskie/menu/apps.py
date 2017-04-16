# coding=utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MenuConfig(AppConfig):
    name = 'petycja_norweskie.menu'
    verbose_name = _("Menu module")
