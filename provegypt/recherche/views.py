import cgitb

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Recherche
# Create your views here.


# / Recherche
def index(request):
    '''proverbes = Proverbe.objects.all()
    proverbes_names_and_versions = [proverbe.nom + " - VAR : " + proverbe.version_ar +
                       " - VFRA : " + proverbe.version_fra for proverbe in proverbes]
    proverbes_names_and_versions_str = ", ".join(proverbes_names_and_versions)
    return HttpResponse("Les proverbes et expressions : " + proverbes_names_and_versions_str)'''
    if 'q' in request.GET:
        q = request.GET['q']
        # recherche = Recherche.objects.filter(version_fra__icontains=q)
        multiple_q = Q(Q(version_fra__icontains=q) | Q(version_ar__icontains=q))
        recherche = Recherche.objects.filter(multiple_q)
    else:
        recherche = Recherche.objects.all().order_by('nom')
    return render(request, 'recherche/index.html', {'recherches': recherche})


