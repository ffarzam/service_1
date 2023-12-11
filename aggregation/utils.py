from dumpdata.models import Raw
from config import settings


def get_related_queryset(arg):
    return Raw.objects.values(arg).annotate(
        kpi_1=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_1"]]("kpi_1"),
        kpi_2=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_2"]]("kpi_2"),
        kpi_3=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_3"]]("kpi_3"),
        kpi_4=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_4"]]("kpi_4"),
        kpi_5=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_5"]]("kpi_5"),
        kpi_6=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_6"]]("kpi_6"),
        kpi_7=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_7"]]("kpi_7"),
        kpi_8=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_8"]]("kpi_8"),
        kpi_9=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_9"]]("kpi_9"),
        kpi_10=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_10"]]("kpi_10"),
        kpi_11=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_11"]]("kpi_11"),
        kpi_12=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_12"]]("kpi_12"),
        kpi_13=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_13"]]("kpi_13"),
        kpi_14=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_14"]]("kpi_14"),
        kpi_15=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_15"]]("kpi_15"),
        kpi_16=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_16"]]("kpi_16"),
        kpi_17=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_17"]]("kpi_17"),
        kpi_18=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_18"]]("kpi_18"),
        kpi_19=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_19"]]("kpi_19"),
        kpi_20=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_20"]]("kpi_20"),
    )