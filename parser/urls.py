from django.urls import path
from . import views

#FOR CORE APP
app_name = "parser"

urlpatterns = [
    path("", views.index, name = "index"),
    path("add/<str:title>/<str:content>", views.add, name = "add")
]
