from django.shortcuts import render
from mywatchlist.models import ListOfFilm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_my_watch_list(request):
    return render(request, "mywatchlist.html", context)

data_film = ListOfFilm.objects.all()
context = {
    'list_film': data_film,
    'namaku': 'Valencius Apriady Primayudha',
    'idku': '2106750830',
}

def show_xml(request):
    data = ListOfFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ListOfFilm.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ListOfFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ListOfFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
