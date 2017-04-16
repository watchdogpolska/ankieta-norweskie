# coding=utf-8
from unittest import TestCase

from django.test import TestCase, RequestFactory

# Create your tests here.
from django.urls import reverse

from petycja_norweskie.campaigns.tests.factories import CampaignFactory
from petycja_norweskie.petitions.tests.factories import SignatureFactory, PetitionFactory


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
