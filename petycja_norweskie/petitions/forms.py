# coding=utf-8

# -*- coding: utf-8 -*-
from django import forms
from .models import Signature, Permission


class SignatureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.petition = kwargs.pop("petition")
        super(SignatureForm, self).__init__(*args, **kwargs)
        if not self.petition.ask_first_name:
            del self.fields['first_name']
        if not self.petition.ask_second_name:
            del self.fields['second_name']
        if not self.petition.ask_organization:
            del self.fields['organization']
        if not self.petition.ask_city:
            del self.fields['city']

        for definition in self.petition.permissiondefinition_set.all():
            field = forms.BooleanField(required=definition.required,
                                       label=definition.text,
                                       initial=definition.default)
            self.fields[self.get_definition_field_name(definition)] = field

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
            if self.cleaned_data[self.get_definition_field_name(definition)]:
                perm = Permission(signature=obj, definition=definition)
                permissions.append(perm)
        Permission.objects.bulk_create(permissions)
