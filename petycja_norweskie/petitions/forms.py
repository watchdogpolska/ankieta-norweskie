# coding=utf-8

# -*- coding: utf-8 -*-
from atom.ext.crispy_forms.forms import SingleButtonMixin
from crispy_forms.layout import Field
from crispy_forms.layout import Layout
from django import forms
from django.urls import reverse

from .models import Signature, Permission


class SignatureForm(SingleButtonMixin, forms.ModelForm):
    @property
    def action_text(self):
        return self.petition.sign_button_text

    def __init__(self, *args, **kwargs):
        self.petition = kwargs.pop("petition")
        self.campaign = kwargs.pop("campaign")

        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse("petitions:form", kwargs={'slug': self.petition.slug})

        self.hide_fields_or_set_label()

        self.set_fields_label_as_placeholder()

        self.append_permissions_field()

    def append_permissions_field(self):
        for definition in self.petition.permissiondefinition_set.all():
            field = forms.BooleanField(required=definition.required,
                                       label=definition.text,
                                       initial=definition.default)
            self.fields[self.get_definition_field_name(definition)] = field

    def hide_fields_or_set_label(self):
        for name in ['first_name', 'second_name', 'organization', 'city', 'email']:
            if getattr(self.petition, 'ask_{}'.format(name)):
                self.fields[name].label = getattr(self.petition, '{}_label'.format(name))
                self.fields[name].required = True
            else:
                del self.fields[name]

    def set_fields_label_as_placeholder(self):
        field_template = "petitions/{}/field_custom.html".format(self.campaign.theme.prefix)
        self.helper.layout = Layout(*[Field(field_name,
                                            template=field_template,
                                            placeholder=field.label)
                                      for field_name, field in self.fields.items()])

    def get_definition_field_name(self, definition):
        return 'permission_{}'.format(definition.pk)

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'organization', 'city', 'email']

    def save(self, commit=True):
        self.instance.petition = self.petition
        obj = super(SignatureForm, self).save(True)
        self.save_permissions(obj)
        return obj

    def save_permissions(self, obj):
        permissions = []
        for definition in self.petition.permissiondefinition_set.all():
            perm = Permission(signature=obj,
                              definition=definition,
                              value=self.cleaned_data[self.get_definition_field_name(definition)])
            permissions.append(perm)
        Permission.objects.bulk_create(permissions)
