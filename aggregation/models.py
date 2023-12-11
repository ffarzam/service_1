from django.db import models

from dumpdata.models import KPI


# Create your models here.


class Site(KPI):
    site = models.CharField(max_length=25, unique=True)


class Province(KPI):
    province = models.CharField(max_length=100, unique=True)


class City(KPI):
    city = models.CharField(max_length=100, unique=True)
