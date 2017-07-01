from test_plus.test import TestCase
from atom.mixins import AdminTestCaseMixin

from petycja_norweskie.menu.models import Element
from petycja_norweskie.menu.tests.factories import ElementFactory
from petycja_norweskie.petitions.models import Petition, Signature
from petycja_norweskie.users.tests.factories import UserFactory


class ElementAdminTestCase(AdminTestCaseMixin, TestCase):
    user_factory_cls = UserFactory
    factory_cls = ElementFactory
    model = Element
