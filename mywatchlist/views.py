from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_film = MyWatchList.objects.all()
def show_my_watch_list(request):
    have_watched = 0
    not_watch = 0
    for iterasi in data_film:
        if iterasi.watched:
            have_watched += 1
        else:
            not_watch+= 1
    if have_watched >= not_watch:
        extra_msg = "Selamat, kamu sudah banyak menonton!"
    else:
        extra_msg = "Wah, kamu masih sedikit menonton!"
        
    context = {
        'message': extra_msg,
        'list_film': data_film,
        'namaku': 'Valencius Apriady Primayudha',
        'idku': '2106750830',
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
