from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Site, City

from .utils import get_related_queryset


# Create your views here.


class FillSiteTableView(APIView):

    def get(self, request):
        data = get_related_queryset("site")

        site_obj =(Site(**item) for item in data)

        Site.objects.bulk_create(site_obj, ignore_conflicts=True)
        return Response({"message": "site table was created"}, status=status.HTTP_200_OK)


class FillCityTableView(APIView):

    def get(self, request):
        data = get_related_queryset("city")

        city_obj =(City(**item) for item in data)

        City.objects.bulk_create(city_obj, ignore_conflicts=True)
        return Response({"message": "city table was created"}, status=status.HTTP_200_OK)
