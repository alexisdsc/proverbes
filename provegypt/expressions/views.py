from django.shortcuts import render
from django.http import HttpResponse
from .models import Expression
# Create your views here.


# / expression
def index(request):
    '''proverbes = Proverbe.objects.all()
    proverbes_names_and_versions = [proverbe.nom + " - VAR : " + proverbe.version_ar +
                       " - VFRA : " + proverbe.version_fra for proverbe in proverbes]
    proverbes_names_and_versions_str = ", ".join(proverbes_names_and_versions)
    return HttpResponse("Les proverbes et expressions : " + proverbes_names_and_versions_str)'''
    expressions = Expression.objects.all().order_by('nom')
    return render(request, 'expressions/index.html', {'expressions': expressions})


