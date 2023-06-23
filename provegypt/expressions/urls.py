from django.urls import path
from . import views


app_name = 'expressions'

urlpatterns = [
    path('', views.index, name="index"),
]