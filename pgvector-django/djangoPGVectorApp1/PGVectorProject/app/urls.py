from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("i2", views.indexTwo, name="indexTwo"),
]