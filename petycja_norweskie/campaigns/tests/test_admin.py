from test_plus.test import TestCase
from atom.mixins import AdminTestCaseMixin

from petycja_norweskie.campaigns.models import Campaign
from petycja_norweskie.campaigns.tests.factories import CampaignFactory
from petycja_norweskie.users.tests.factories import UserFactory


class CampaignAdminTestCase(AdminTestCaseMixin, TestCase):
    user_factory_cls = UserFactory
    factory_cls = CampaignFactory
    model = Campaign
