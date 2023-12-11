from django.db import models

from dumpdata.models import KPI


# Create your models here.


class Site(KPI):
    site = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.site}"


class Province(KPI):
    province = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.province}"


class City(KPI):
    city = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.city}"
