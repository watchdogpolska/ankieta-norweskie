# coding=utf-8
from django.contrib import admin

# Register your models here.
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ExportMixin

from petycja_norweskie.petitions.models import Petition, PermissionDefinition, Signature, Permission
from petycja_norweskie.petitions.resources import SignatureResource


class PermissionDefinitionInline(admin.TabularInline):
    model = PermissionDefinition


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'ask_first_name', 'ask_second_name', 'ask_organization', 'ask_city',
                    'get_permissiondefinition_count', 'get_signature_count')
    inlines = [
        PermissionDefinitionInline,
    ]
    search_fields = ('title', 'text')

    def get_signature_count(self, obj):
        return obj.signature_count
    get_signature_count.short_description = _('Signature count')

    def get_permissiondefinition_count(self, obj):
        return obj.definition_count
    get_permissiondefinition_count.short_description = _("Permission definition count")

    def get_queryset(self, request):
        return super(PetitionAdmin, self).get_queryset(request).annotate(signature_count=Count('signature'),
                                                                         definition_count=Count('permissiondefinition'))


class PermissionInline(admin.TabularInline):
    model = Permission


@admin.register(Signature)
class SignatureAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = SignatureResource
    list_display = ('pk', 'first_name', 'second_name', 'organization', 'city')
    inlines = [
        PermissionInline
    ]
