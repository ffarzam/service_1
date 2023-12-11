from django.db import models

# Create your models here.


class KPI(models.Model):
    kpi_1 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_2 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_3 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_4 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_5 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_6 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_7 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_8 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_9 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_10 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_11 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_12 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_13 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_14 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_15 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_16 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_17 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_18 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_19 = models.DecimalField(max_digits=19, decimal_places=10)
    kpi_20 = models.DecimalField(max_digits=19, decimal_places=10)

    class Meta:
        abstract = True


class Site(KPI):
    site = models.CharField(max_length=25, unique=True)


class Province(KPI):
    province = models.CharField(max_length=100, unique=True)


class City(KPI):
    city = models.CharField(max_length=100, unique=True)