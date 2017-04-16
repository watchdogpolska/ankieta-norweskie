# coding=utf-8
import factory
from django.conf import settings
from django.contrib.sites.models import Site

from petycja_norweskie.campaigns.models import Campaign
from petycja_norweskie.themes.models import Theme


class CampaignFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence('campaign-{0}'.format)
    organizer = factory.Sequence('organizer-{0}'.format)

    theme = factory.Iterator(Theme.objects.all())

    site_title = factory.Sequence('site-{0}'.format)
    site_subtitle = factory.Sequence('subtitle-{0}'.format)

    show_title = factory.Sequence(lambda n: n % 2 == 0)

    site = factory.Iterator(Site.objects.all())

    class Meta:
        model = Campaign
        django_get_or_create = ('name', )
