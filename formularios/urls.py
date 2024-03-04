from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'formularios'

urlpatterns = [
    path("formTX/", views.formularioTX_view, name="formularioTX"),
    path("success/", views.form_success, name="success"),
    # path('upload', UploadView.as_view(), name='upload'),


]
