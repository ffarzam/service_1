from django.urls import path

from . import views

urlpatterns = [
    path('site/', views.FillSiteTableView.as_view(), name="site"),
    path('city/', views.FillCityTableView.as_view(), name="city"),
    path('province/', views.FillProvinceTableView.as_view(), name="province"),
]