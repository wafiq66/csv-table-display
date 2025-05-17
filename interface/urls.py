from django.urls import path,include
from . import views

urlpatterns = [
    path("interface/", views.view_table, name="view_table"),
]