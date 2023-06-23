from django.urls import path
from . import views


app_name = 'proverbe'

urlpatterns = [
    path('', views.index, name="index"),

]