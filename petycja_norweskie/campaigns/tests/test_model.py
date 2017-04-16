# coding=utf-8
from unittest import TestCase

from petycja_norweskie.campaigns.tests.factories import CampaignFactory


class CampaignTestCase(TestCase):
    def test_factory_create(self):
        CampaignFactory()
