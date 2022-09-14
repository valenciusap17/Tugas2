from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'namaku': 'Valencius Apriady Primayudha',
    'idku': '2106750830',
}