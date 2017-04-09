# coding=utf-8

from django.test import TestCase, RequestFactory

# Create your tests here.
from petycja_norweskie.petitions.views import SignatureListView


class TestSignatureListView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_context_data(self):
        request = self.factory.get("/")
        response = SignatureListView.as_view()(request)
        self.assertIn(response.context_data, 'form')
        self.assertIn(response.context_data, 'petition')

    # def test_get_queryset(self):
    #     request = self.factory.get("/")
    #     response = SignatureListView.as_view()(request)

