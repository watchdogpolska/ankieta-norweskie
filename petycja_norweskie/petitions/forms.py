# coding=utf-8

# -*- coding: utf-8 -*-
from atom.ext.crispy_forms.forms import SingleButtonMixin
from crispy_forms.layout import Layout
from django import forms
from django.urls import reverse
from crispy_forms.layout import Field
from .models import Signature, Permission


class SignatureForm(SingleButtonMixin, forms.ModelForm):

    @property
    def action_text(self):
        return self.petition.sign_button_text

    def __init__(self, *args, **kwargs):
        self.petition = kwargs.pop("petition")
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse("petitions:form", kwargs={'slug': self.petition.slug})
        if not self.petition.ask_first_name:
            del self.fields['first_name']
        if not self.petition.ask_second_name:
            del self.fields['second_name']
        if not self.petition.ask_organization:
            del self.fields['organization']
        if not self.petition.ask_city:
            del self.fields['city']
        if not self.petition.ask_email:
            del self.fields['email']

        self.helper.layout = Layout(*[Field(field_name,
                                            template="petitions/field_custom.html",
                                            placeholder=field.label)
                                      for field_name, field in self.fields.items()])

        for definition in self.petition.permissiondefinition_set.all():
            field = forms.BooleanField(required=definition.required,
                                       label=definition.text,
                                       initial=definition.default)
            self.fields[self.get_definition_field_name(definition)] = field

        # self.helper.layout = self.helper.build_default_layout(self)

    def get_definition_field_name(self, definition):
        return 'permission_{}'.format(definition.pk)

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'organization', 'city']

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
