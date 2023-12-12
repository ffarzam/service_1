from dumpdata.models import Raw
from config import settings

from dumpdata.models import KPI

from .models import Site, City, Province


def get_related_queryset(arg):
    my_dict = {}
    number_of_fields = len(KPI._meta.get_fields())
    for i in range(1, number_of_fields + 1):
        my_dict.update({f"kpi_{i}": settings.AGGREGATION_MAPPER[settings.AGGREGATION[f"kpi_{i}"]](f"kpi_{i}")})
    return Raw.objects.values(arg).annotate(**my_dict)


def model_mapper(arg):
    mapper = {
        "site": Site,
        "city": City,
        "province": Province
    }
    return mapper[arg]
