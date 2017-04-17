# coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _



class PetitionConfig(AppConfig):
    name = 'petycja_norweskie.petitions'
    verbose_name = _("Petition")

    def ready(self):
        from petycja_norweskie.petitions.models import update_counter, Signature
        pre_save.connect(update_counter, Signature)
