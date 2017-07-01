from test_plus.test import TestCase
from atom.mixins import AdminTestCaseMixin

from petycja_norweskie.petitions.models import Petition, Signature
from petycja_norweskie.petitions.tests.factories import PetitionFactory, SignatureFactory
from petycja_norweskie.users.tests.factories import UserFactory


class PetitionAdminTestCase(AdminTestCaseMixin, TestCase):
    user_factory_cls = UserFactory
    factory_cls = PetitionFactory
    model = Petition


class SignatureAdminTestCase(AdminTestCaseMixin, TestCase):
    user_factory_cls = UserFactory
    factory_cls = SignatureFactory
    model = Signature
