from django.urls import path, include
from . import views

app_name = "godalem"

urlpatterns = [
    path("", views.index, name="index"),
    path("request-meter/", views.request_meter, name="request-meter"),
    path("buy-power/", views.buy_power, name="buy-power"),
]