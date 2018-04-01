from django.shortcuts import render
from django.http import HttpResponse , Http404
from .models import Substation


# Create your views here.


def index(request):
    all_substations = Substation.objects.all()
    return render(request, 'project/index.html', {'all_substations': all_substations})


def detail(request, substation_id):
    try:
        substation = Substation.objects.get(pk=substation_id)
    except Substation.DoesNotExist:
        raise Http404("Substation not in the list")
    return render(request , 'project/details.html', {'substation': substation})
