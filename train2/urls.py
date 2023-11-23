from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name = "booking"),
    path("booking", views.booking, name = "booking"),
    path("status", views.status, name = "status"),
    path("search_by_name", views.search_by_name, name = "search_by_name"),
    path("search_by_station", views.search_by_station, name = "search_by_station"),
    path("search", views.search, name = "search")

]