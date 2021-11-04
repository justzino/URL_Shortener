from django.urls import path

from .views import index_view

appname = "shortener"

urlpatterns = [
    path("", index_view, name="index"),
]
