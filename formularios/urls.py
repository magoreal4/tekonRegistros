from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'formularios'

urlpatterns = [
    path("form1/", views.formulario1_view, name="form1"),
    path("success/", views.form_success, name="success"),
]
