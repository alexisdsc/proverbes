from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Proverbe
# Create your views here.


# / proverbe
def index(request):
    '''proverbes = Proverbe.objects.all()
    proverbes_names_and_versions = [proverbe.nom + " - VAR : " + proverbe.version_ar +
                       " - VFRA : " + proverbe.version_fra for proverbe in proverbes]
    proverbes_names_and_versions_str = ", ".join(proverbes_names_and_versions)
    return HttpResponse("Les proverbes et expressions : " + proverbes_names_and_versions_str)'''
    proverbes = Proverbe.objects.all().order_by('nom')
    return render(request, 'proverbe/index.html', {'proverbes': proverbes})


def api_get_proverbes(request):
    proverbes = Proverbe.objects.all().order_by('nom')
    json = serializers.serialize("json", proverbes)
    return HttpResponse(json)

