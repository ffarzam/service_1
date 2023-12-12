from django.db import models

from dumpdata.models import KPI

from .mixins import ItemsMixin


# Create your models here.


class Site(ItemsMixin, KPI):
    site = models.CharField(max_length=25, unique=True)

    @classmethod
    def get_queryset_with_in_operator(cls, elements):
        return cls.objects.filter(site__in=elements)

    def __str__(self):
        return f"{self.site}"


class Province(ItemsMixin, KPI):
    province = models.CharField(max_length=100, unique=True)

    @classmethod
    def get_queryset_with_in_operator(cls, elements):
        return cls.objects.filter(province__in=elements)

    def __str__(self):
        return f"{self.province}"


class City(ItemsMixin, KPI):
    city = models.CharField(max_length=100, unique=True)

    @classmethod
    def get_queryset_with_in_operator(cls, elements):
        return cls.objects.filter(city__in=elements)

    def __str__(self):
        return f"{self.city}"
