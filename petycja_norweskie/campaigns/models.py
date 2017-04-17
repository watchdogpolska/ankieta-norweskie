# coding=utf-8
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel

from petycja_norweskie.themes.models import Theme
from petycja_norweskie.users.models import User


class CampaignQuerySet(models.QuerySet):
    def for_admin(self, user: User):
        if user.is_superuser:
            return self
        return self.filter(users=user)


class Campaign(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"),
                            max_length=100)
    organizer = models.CharField(verbose_name=_("Organizer"),
                                 max_length=250,
                                 help_text=_("Person or organization responsible for campaign organization"))
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    site = models.OneToOneField(Site,
                                verbose_name=_("Site"),
                                help_text=_("Sites used in campaign"),
                                on_delete=models.CASCADE)
    site_title = models.CharField(verbose_name=_("Name"),
                                  max_length=150)
    site_subtitle = models.CharField(verbose_name=_("Subtitle"),
                                     max_length=150)

    users = models.ManyToManyField(to=User, verbose_name=_("Users"),
                                   help_text=_("Users responsive to manage of campaign"))

    show_title = models.BooleanField(default=True,
                                     help_text=_("Show title of petition"))

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")
        ordering = ['created', ]

    def __str__(self):
        return self.name
