from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/csv-upload', views.medicamento_upload, name="medicamento_upload"),
]