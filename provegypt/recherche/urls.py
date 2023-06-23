from django.urls import path, include
from . import views


app_name = 'recherche'

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('proverbe.urls', 'expressions.urls')),
]