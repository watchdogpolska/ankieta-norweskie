# coding=utf-8
from django.test import TestCase

from petycja_norweskie.campaigns.tests.factories import CampaignFactory
from petycja_norweskie.petitions.tests.factories import SignatureFactory, PetitionFactory

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse


class HomePageTestCase(TestCase):
    def test_get_redirect_url(self):
        campaign = CampaignFactory()
        petition_front = PetitionFactory(campaign=campaign, front=True)
        PetitionFactory(campaign=campaign, front=False)  # extra petition
        response = self.client.get("/")
        self.assertRedirects(response, petition_front.get_absolute_url())


class TestSignatureListView(TestCase):
    def setUp(self):
        self.signature = SignatureFactory(petition__is_active=True)
        self.url = reverse('petitions:signature', kwargs={'slug': self.signature.petition.slug})

    def test_page_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestPetitionDetailView(TestCase):
    def setUp(self):
        self.petition = PetitionFactory(is_active=True)
        self.url = self.petition.get_absolute_url()

    def test_page_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class SignatureFormViewTestCase(TestCase):
    def setUp(self):
        self.petition = PetitionFactory(is_active=True,
                                        ask_first_name=True,
                                        ask_second_name=False,
                                        ask_organization=False,
                                        ask_city=False,
                                        ask_email=False)
        self.url = reverse('petitions:form', kwargs={'slug': self.petition.slug})
        self.success_url = reverse('petitions:success', kwargs={'slug': self.petition.slug})

    def test_page_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_form_submit(self):
        response = self.client.post(self.url, {'first_name': "X"})
        self.assertRedirects(response, self.success_url)

    def test_petition_disabled(self):
        self.petition.is_active = False
        self.petition.save()
        response = self.client.post(self.url, {'first_name': "X"}, follow=True)
        self.assertRedirects(response, self.petition.get_absolute_url())
        self.assertMessageContains(response, "warning", self.petition.disabled_warning)

    def assertMessageContains(self, response, type, msg):
        try:
            message = list(response.context['messages'])[0]
        except AttributeError:  # since django 1.11 it available as context_data
            message = list(response.context_data.get('messages'))[0]

        self.assertEqual(message.tags, type)
        self.assertTrue(msg in message.message)


class PetitionSuccessViewTestCase(TestCase):
    def setUp(self):
        self.petition = PetitionFactory()
        self.url = reverse('petitions:success', kwargs={'slug': self.petition.slug})

    def test_page_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_page_contains_greetings(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.petition.finish_message)
