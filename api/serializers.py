import re

from django.apps import apps
from rest_framework import serializers

from aggregation.utils import model_mapper


class APISerializer(serializers.Serializer):
    layer = serializers.CharField()
    elements = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    kpi = serializers.CharField()

    def validate_kpi(self, value):
        character_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                          "k", "p", "i", "_", "(", ")", "/", "*", "-", "+", " "]
        for i in value:
            if i not in character_list:
                raise serializers.ValidationError("invalid input in kpi formula")

        valid_matches = re.findall(r'\bkpi_(?:[1-9]|1[0-9]|20)\b', value)
        all_matches = re.findall(r'\b\w*?kpi\w*\b', value)
        if valid_matches != all_matches:
            raise serializers.ValidationError("invalid input in kpi formula")
        return value

    def validate_layer(self, value):
        app_models = apps.get_app_config('aggregation').get_models()
        models_name_list = list(map(lambda x: x.__name__.lower(), app_models))
        if value not in models_name_list:
            raise serializers.ValidationError("invalid layer input")
        model = model_mapper(value)
        return model

    def validate(self, data):

        model = data["layer"]
        elements = data["elements"]
        qs = model.get_queryset_with_in_operator(elements)
        if not qs.exists():
            raise serializers.ValidationError("invalid elements input")
        data["elements"] = qs
        return data
