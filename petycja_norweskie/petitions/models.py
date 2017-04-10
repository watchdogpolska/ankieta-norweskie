# coding=utf-8


from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from petycja_norweskie.users.models import User


class PetitionQuerySet(models.QuerySet):
    def for_user(self, user: User):
        if user.is_anonymous():
            return self.filter(is_active=True)
        return self


@python_2_unicode_compatible
class Petition(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    slug = models.CharField(verbose_name=_("Slug"), max_length=50, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=250)
    text = models.TextField(verbose_name=_("Text"))
    ask_first_name = models.BooleanField(verbose_name=_("Ask first name"), default=False)
    ask_second_name = models.BooleanField(verbose_name=_("Ask second name"), default=False)
    ask_organization = models.BooleanField(verbose_name=_("Ask organization"), default=True)
    ask_city = models.BooleanField(verbose_name=_("Ask about city"))
    objects = PetitionQuerySet.as_manager()
    paginate_by = models.SmallIntegerField(default=50, verbose_name=_("Paginate by"))
    is_published = models.BooleanField(default=False, verbose_name=_("Is published on site?"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is open to new signatures?"))
    front = models.BooleanField(default=True,
                                verbose_name=_("Is available on front-view?"),
                                help_text=_("There should be only one available sites"))
    finish_message = models.TextField(verbose_name=_("Finish message"), help_text=_("Messages shows after signatures"))
    sign_button_text = models.CharField(max_length=50, default=_("Sign"))

    class Meta:
        verbose_name = _("Petition")
        verbose_name_plural = _("Petitions")
        ordering = ['created', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('petitions:petition', kwargs={'slug': self.slug})


class PermissionDefinition(models.Model):
    petition = models.ForeignKey(Petition, help_text=_("Petition"))
    text = models.TextField()
    default = models.BooleanField(default=True, help_text=_("Define default check on permission field"))
    required = models.BooleanField(default=True, help_text=_("Define the field is required or not"))
    ordering = models.PositiveSmallIntegerField(default=1, help_text=_("Define orders of the permissions in form"))

    class Meta:
        verbose_name = _("Definition")
        verbose_name_plural = _("Definitions")


class SignatureQuerySet(models.QuerySet):
    pass


@python_2_unicode_compatible
class Signature(TimeStampedModel):
    petition = models.ForeignKey(Petition, verbose_name=_("Petition"))
    first_name = models.CharField(max_length=50, blank=True, verbose_name=_("First name"))
    second_name = models.CharField(max_length=50, blank=True, verbose_name=_("Second name"))
    organization = models.CharField(max_length=100, blank=True, verbose_name=_("Organization"))
    city = models.CharField(max_length=50, blank=True, verbose_name=_("City"))

    objects = SignatureQuerySet.as_manager()

    class Meta:
        verbose_name = _("Signature")
        verbose_name_plural = _("Signatures")
        ordering = ['created', ]

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name) or self.organization


class Permission(models.Model):
    definition = models.ForeignKey(PermissionDefinition, verbose_name=_("Definition"))
    signature = models.ForeignKey(Signature, verbose_name=_("Signature"))
    value = models.BooleanField(verbose_name=_("Value"))

    class Meta:
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")
