import re

from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from aggregation.utils import model_mapper

from .serializers import APISerializer


# Create your views here.


class KPICalculatorView(APIView):
    """
        A custom API view that processes GET requests to calculate KPIs based on the provided layer, elements
        and KPI formula.

        Parameters:
        - request: The HTTP GET request object.

        Expected JSON data in the request:
        {
            "layer": "layer_name"
            "elements": ["element1", "element2"],
            "kpi": "some formula "
        }

        Returns:
        - Response: A JSON response containing the calculated KPIs for each element.

        Example:
        To use this view, send a GET request with the required parameters in the JSON data:
        ```
        GET /the_endpoint/
        {
            "layer": "city"
            "elements": ["SARI", "YAZD"],
            "kpi": "(kpi_1 + kpi_2) / kpi_3"
        }
        ```
        The response will be a JSON object with the calculated KPIs for each element:
        ```
        {
            "SARI": 5.0,
            "YAZD": 8.0
        }
        ```
    """

    serializer_class = APISerializer

    def get(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        elements = serializer.validated_data["elements"]
        kpi_formula = serializer.validated_data["kpi"]

        valid_matches = re.findall(r'\bkpi_(?:[1-9]|1[0-9]|20)\b', kpi_formula)

        my_dict = {}
        result_dict = {}
        for item in elements:
            for kpi in valid_matches:
                my_dict.update({kpi: item.get_kpi(kpi)})
            res = eval(kpi_formula, my_dict)
            result_dict.update({f"{item}": res})
            my_dict = {}

        return Response(result_dict, status=status.HTTP_200_OK)
