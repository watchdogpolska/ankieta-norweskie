# coding=utf-8
from django.contrib import admin
# Register your models here.
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ExportMixin

from petycja_norweskie.campaigns.models import Campaign
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
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'title', 'text', 'finish_message', 'overview')
        }),
        (_("Publication"), {'fields': ('is_published', 'is_active', 'front')}),
        (_('Form'), {
            'description': _("Configuration on signature submit form"),
            'fields': (('ask_first_name', 'first_name_label'),
                       ('ask_second_name', 'second_name_label'),
                       ('ask_organization', 'organization_label'),
                       ('ask_city', 'city_label'),
                       ('ask_email', 'email_label'),
                       'sign_button_text')
        }),
        (_('Advanced'), {
            'fields': ('paginate_by', 'campaign')
        }),

    )

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "campaign":
            kwargs["choices"] = Campaign.objects.for_admin(self.request.user).all()
        return super().formfield_for_choice_field(db_field, request, **kwargs)

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
    list_display = ('pk', 'counter', 'first_name', 'second_name', 'organization', 'city', 'email')
    inlines = [
        PermissionInline
    ]
    readonly_fields = ('counter', )
