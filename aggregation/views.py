from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dumpdata.models import Raw

from .models import Site

from config import settings


# Create your views here.


class FillSiteTableView(APIView):

    def get(self, request):
        data = Raw.objects.values("site").annotate(kpi_1=settings.AGGREGATION_MAPPER[settings.AGGREGATION["kpi_1"]]("kpi_1"),
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

        site_obj =(Site(**item) for item in data)

        Site.objects.bulk_create(site_obj, ignore_conflicts=True)
        return Response({"message": "site table was created"}, status=status.HTTP_200_OK)

