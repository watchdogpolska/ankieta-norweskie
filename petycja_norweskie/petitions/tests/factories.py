# coding=utf-8

import factory
import factory.fuzzy


class PetitionFactory(factory.django.DjangoModelFactory):
    campaign = factory.SubFactory("petycja_norweskie.campaigns.tests.factories.CampaignFactory")
    name = factory.Sequence("petition-name-{0}".format)
    slug = factory.Sequence("petition-slug-{0}".format)
    title = factory.Sequence("petition-title-{0}".format)
    text = factory.fuzzy.FuzzyText()
    overview = factory.fuzzy.FuzzyText()
    finish_message = factory.fuzzy.FuzzyText()
    ask_first_name = factory.Sequence(lambda n: n % 2 == 0)
    ask_second_name = factory.Sequence(lambda n: n % 2 == 0)
    ask_organization = factory.Sequence(lambda n: n % 2 == 0)
    ask_city = factory.Sequence(lambda n: n % 2 == 0)
    ask_email = factory.Sequence(lambda n: n % 2 == 0)
    first_name_label = factory.Sequence("petition-first_name_label-{0}".format)
    second_name_label = factory.Sequence("petition-second_name_label-{0}".format)
    organization_label = factory.Sequence("petition-organization_label-{0}".format)
    city_label = factory.Sequence("petition-city_label-{0}".format)
    email_label = factory.Sequence("petition-email_label-{0}".format)
    sign_button_text = factory.Sequence("petition-sign_button_text-{0}".format)
    paginate_by = factory.Sequence(lambda n: n)
    is_published = True
    is_active = True
    disabled_warning = factory.fuzzy.FuzzyText()
    disabled_message = factory.fuzzy.FuzzyText()

    front = factory.Sequence(lambda n: n % 2 == 0)

    class Meta:
        model = 'petitions.Petition'


class SignatureFactory(factory.django.DjangoModelFactory):
    petition = factory.SubFactory("petycja_norweskie.petitions.tests.factories.PetitionFactory")
    first_name = factory.Sequence("signature-first_name-{0}".format)
    second_name = factory.Sequence("signature-second_name-{0}".format)
    organization = factory.Sequence("signature-organization-{0}".format)
    city = factory.Sequence("signature-city-{0}".format)
    email = factory.Sequence("signature-email-{0}".format)

    class Meta:
        model = 'petitions.Signature'


class PermissionDefinitionFactory(factory.django.DjangoModelFactory):
    petition = factory.SubFactory("petycja_norweskie.petitions.tests.factories.PetitionFactory")
    text = factory.fuzzy.FuzzyText()
    default = factory.Sequence(lambda n: n % 2 == 0)
    required = factory.Sequence(lambda n: n % 2 == 0)
    ordering = factory.Sequence(lambda n: n)

    class Meta:
        model = 'petitions.PermissionDefinition'


class PermissionFactory(factory.django.DjangoModelFactory):
    definition = factory.SubFactory("petycja_norweskie.petitions.tests.factories.PermissionDefinitionFactory")
    signature = factory.SubFactory("petycja_norweskie.petitions.tests.factories.SignatureFactory")
    value = factory.Sequence(lambda n: n % 2 == 0)

    class Meta:
        model = 'petitions.Permission'
