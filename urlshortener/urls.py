from django.urls import path

from .views import index_view, redirect_view

appname = "shortener"

urlpatterns = [
    path("", index_view, name="index"),
    path('<str:short_path>', redirect_view, name='redirect'),
]
