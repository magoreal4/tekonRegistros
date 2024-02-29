from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'formularios'

urlpatterns = [
    path("formTX/", views.formularioTX_view, name="formularioTX"),
    path("formPreIng/", views.formularioPreIng_view, name="formularioPreIngenieria"),
    path("success/", views.form_success, name="success"),
]
