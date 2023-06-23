from django.urls import path
from . import views


app_name = 'proverbe'

urlpatterns = [
    path('GetProverbes', views.api_get_proverbes),

]