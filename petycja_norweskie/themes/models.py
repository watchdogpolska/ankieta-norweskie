# coding=utf-8
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class ThemeQuerySet(models.QuerySet):
    pass


class Theme(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Name"))
    authorship = models.CharField(verbose_name=_("Authorship"), max_length=100)
    prefix = models.CharField(max_length=25, verbose_name=_("System name of theme prefix"))
    objects = ThemeQuerySet.as_manager()

    class Meta:
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")
        ordering = ['created', ]

    def __str__(self):
        return self.name
