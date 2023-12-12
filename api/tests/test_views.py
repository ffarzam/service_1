from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from config import settings
from aggregation.models import Site, City, Province  # Import your actual model
from decimal import Decimal

from dumpdata.models import KPI

from api.serializers import APISerializer


class KPICalculatorViewTest(APITestCase):
    def setUp(self):
        kpi_dict = {}
        number_of_fields = len(KPI._meta.get_fields())
        for j in range(1, number_of_fields + 1):
            kpi_dict.update({f"kpi_{j}": Decimal(f"0.{j}")})
        Site.objects.create(site="S001", **kpi_dict)
        Site.objects.create(site="S002", **kpi_dict)
        City.objects.create(city="RASHT", **kpi_dict)
        City.objects.create(city="TEHRAN", **kpi_dict)
        Province.objects.create(province="GILAN", **kpi_dict)
        Province.objects.create(province="Tehran", **kpi_dict)

    def tearDown(self):
        Site.objects.all().delete()
        City.objects.all().delete()
        Province.objects.all().delete()

    def test_kpi_calculator_view_for_city(self):
        kpi_calculator_url = reverse("kpi_calculator")
        data = {
            "layer": "city",
            "elements": ["RASHT"],
            "kpi": "kpi_1 + kpi_2"
        }
        serializer = APISerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        response = self.client.get(kpi_calculator_url, data=data, format='json')
        obj = City.objects.get(city="RASHT")
        kpi = obj.kpi_1 + obj.kpi_1

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["RASHT"], float(kpi))

    def test_kpi_calculator_view_empty_elements(self):
        kpi_calculator_url = reverse("kpi_calculator")
        data = {
            "layer": "city",
            "elements": [],
            "kpi": "kpi_1 + kpi_2"
        }
        serializer = APISerializer(data=data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.errors["elements"][0].title(), "This List May Not Be Empty.")
        response = self.client.get(kpi_calculator_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_kpi_calculator_view_invalid_elements(self):
        kpi_calculator_url = reverse("kpi_calculator")
        data = {
            "layer": "city",
            "elements": ["invalid"],
            "kpi": "kpi_1 + kpi_2"
        }
        serializer = APISerializer(data=data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0].title(), "Invalid Elements Input")
        response = self.client.get(kpi_calculator_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_kpi_calculator_view_invalid_layer(self):
        kpi_calculator_url = reverse("kpi_calculator")
        data = {
            "layer": "invalid",
            "elements": ["RASHT"],
            "kpi": "kpi_1 + kpi_2"
        }
        serializer = APISerializer(data=data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.errors["layer"][0].title(), "Invalid Layer Input")
        response = self.client.get(kpi_calculator_url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_kpi_calculator_view_invalid_kpi(self):
        kpi_calculator_url = reverse("kpi_calculator")
        data = {
            "layer": "invalid",
            "elements": ["RASHT"],
            "kpi": "kpi_1 + kpi_100"
        }
        serializer = APISerializer(data=data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.errors["kpi"][0].title(), "Invalid Input In Kpi Formula")
        response = self.client.get(kpi_calculator_url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



