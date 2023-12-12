from django.urls import path

from . import views

urlpatterns = [
    path('kpi_calculator/', views.KPICalculatorView.as_view(), name="kpi_calculator"),

]