
class ItemsMixin:

    def get_kpi(self, kpi):
        field_object = self.__class__._meta.get_field(kpi)
        return field_object.value_from_object(self)
