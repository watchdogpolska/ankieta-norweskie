from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import Resolver404, resolve


def is_external_url(value):
    return '://' in value


def is_valid_url(value):
    try:
        resolve(value)
    except Resolver404:
        return False
    return True


def is_mail(value: str):
    return value.startswith("mailto:")


def is_external_or_valid_url(value):
    if not (is_external_url(value) or is_valid_url(value) or is_mail(value)):
        raise ValidationError(
            _('%(value)s is neither an external URL or valid internal URL or mailto.'),
            params={'value': value},
        )
