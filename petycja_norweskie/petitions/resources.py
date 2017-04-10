# coding=utf-8
from import_export import resources, fields

from petycja_norweskie.petitions.models import Signature, PermissionDefinition


class PermissionField(fields.Field):
    def get_value(self, obj):
        try:
            return [x for x in obj.permission_set.all() if x.definition == self.attribute][0].value
        except IndexError:
            return "N/N"


class SignatureResource(resources.ModelResource):
    def __init__(self) -> None:
        super().__init__()
        self.add_field()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('permission_set')

    class Meta:
        model = Signature

    def add_field(self):
        for definition in PermissionDefinition.objects.all():
            self.fields[self.get_permission_field_name(definition)] = self.get_permission_field(definition)

    def get_permission_field_name(self, definition):
        return 'definition_{}'.format(definition.pk)

    def get_permission_field(self, definition):
        kwargs = dict(column_name=self.get_permission_field_name(definition),
                      attribute=definition)
        return PermissionField(**kwargs)
