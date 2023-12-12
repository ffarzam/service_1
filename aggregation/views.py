from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Site, City, Province

from .utils import get_related_queryset


# Create your views here.


class FillSiteTableView(APIView):
    """
        A custom API view that dump data related to 'site' from an external source,
        creates Site objects, and bulk inserts them into the Site table in database.

        Endpoint: GET /site/

        Parameters:
        - request: The HTTP GET request object.

        Returns:
        - Response: A JSON response indicating the status of the operation.

        Operation:
        This view retrieves data related to 'site' using the get_related_queryset function,
        creates Site objects from the data, and bulk inserts them into the database using
        the bulk_create method. If conflicts are encountered, they are ignored.

        Example:
        To fill the 'site' table, send a GET request to the endpoint:
        ```
        GET /site/
        ```
        The response will be a JSON object with a message indicating the success of the operation:
        ```
        {
            "message": "site table was created"
        }
        ```
    """

    def get(self, request):
        data = get_related_queryset("site")

        site_obj = (Site(**item) for item in data)

        Site.objects.bulk_create(site_obj, ignore_conflicts=True)
        return Response({"message": "site table was created"}, status=status.HTTP_200_OK)


class FillCityTableView(APIView):
    """
        A custom API view that dump data related to 'city' from an external source,
        creates City objects, and bulk inserts them into the City table in database.

        Endpoint: GET /city/

        Parameters:
        - request: The HTTP GET request object.

        Returns:
        - Response: A JSON response indicating the status of the operation.

        Operation:
        This view retrieves data related to 'city' using the get_related_queryset function,
        creates City objects from the data, and bulk inserts them into the database using
        the bulk_create method. If conflicts are encountered, they are ignored.

        Example:
        To fill the 'city' table, send a GET request to the endpoint:
        ```
        GET /city/
        ```
        The response will be a JSON object with a message indicating the success of the operation:
        ```
        {
            "message": "city table was created"
        }
        ```
    """

    def get(self, request):
        data = get_related_queryset("city")

        city_obj = (City(**item) for item in data)

        City.objects.bulk_create(city_obj, ignore_conflicts=True)
        return Response({"message": "city table was created"}, status=status.HTTP_200_OK)


class FillProvinceTableView(APIView):
    """
        A custom API view that dump data related to 'province' from an external source,
        creates Province objects, and bulk inserts them into the Province table in database.

        Endpoint: GET /province/

        Parameters:
        - request: The HTTP GET request object.

        Returns:
        - Response: A JSON response indicating the status of the operation.

        Operation:
        This view retrieves data related to 'province' using the get_related_queryset function,
        creates Province objects from the data, and bulk inserts them into the database using
        the bulk_create method. If conflicts are encountered, they are ignored.

        Example:
        To fill the 'province' table, send a GET request to the endpoint:
        ```
        GET /province/
        ```
        The response will be a JSON object with a message indicating the success of the operation:
        ```
        {
            "message": "province table was created"
        }
        ```
    """

    def get(self, request):
        data = get_related_queryset("province")

        province_obj = (Province(**item) for item in data)

        Province.objects.bulk_create(province_obj, ignore_conflicts=True)
        return Response({"message": "province table was created"}, status=status.HTTP_200_OK)
