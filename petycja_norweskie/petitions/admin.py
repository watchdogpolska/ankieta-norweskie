# coding=utf-8
from django.contrib import admin

# Register your models here.
from django.db.models import Count

from petycja_norweskie.petitions.models import Petition, PermissionDefinition, Signature, Permission


class PermissionDefinitionInline(admin.StackedInline):
    model = PermissionDefinition


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'ask_first_name', 'ask_second_name', 'ask_organization', 'ask_city')
    inlines = [
        PermissionDefinitionInline,
    ]
    search_fields = ('title', 'text')

    def get_signature_count(self, obj):
        return obj.signature_count

    def get_permissiondefinition_count(self, obj):
        return obj.permissiondefinition_count

    def get_queryset(self, request):
        return super(PetitionAdmin, self).get_queryset(request).annotate(signature_count=Count('signature'),
                                                                         definition_count=Count('permissiondefinition'))


class PermissionInline(admin.StackedInline):
    model = Permission


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'organization', 'city')
    inlines = [
        PermissionInline
    ]
