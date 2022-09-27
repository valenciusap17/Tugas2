# Tugas 3 PBP # 

Link heroku dapat diakses di [sini](https://tugas2pbp-valencius.herokuapp.com/mywatchlist/)

## Perbedaan JSON, XML, dan HTML ##

Pada dasarnya, JSON dan XML memiliki kegunaan yang sama, hanya saja terdapat beberapa perbedaan yang membedakan keduanya. Dari segi cara penyimpanan data, JSON lebih efisien walaupun menghasilkan data yang kurang enak dilihat secara visual, sedangkan XML dapat menyusun data yang lebih terstruktur tetapi kurang efisien. Ekstensi file yang dimiliki oleh XML adalah .xml, sedangkan ekstensi file yang dimiliki oleh JSON adalah .json. JSON digunakan untuk mengirimkan data yang diuraikan terlebih dahulu dan mengirimkannya melalui internet, sementara XML cenderung dimanfaatkan kerapihan datanya untuk membuat catatan. HTML lebih sering dimanfaatkan utnuk menyajikan data.

## mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? ##

Kita memerlukan data delivery untuk mempermudah pengiriman data dari komputer ke platform atau mungkin dari satu platform ke platform lainnya. 

## Cara pengimplementasian checklist di atas ##

### Membuat aplikasi mywatchlist ###
Pertama-tama, kita akan membuat suatu aplikasi baru dengan nama mywatchlist di proyek Tugas 2 pekan lalu. Maka, kita harus change directory kita pada terminal yang kita gunakan menuju folder Tugas2 yang sudah kita miliki sejak pekan lalu. Sebelum kita masuk ke dalam pengimplementasian, kita perlu menyalakan virtual environment terlebih dahulu dengan menjalankan perintah:
```
python -m venv env
env\Scripts\activate.bat
```
Kemudian untuk membuat aplikasi baru kita menjalankan perintah :
```
python manage.py startapp mywatchlist
```

### Menambahkan path mywatchlist ###
Untuk checklist selanjutnya, agar kita bisa mengakses ``` http://localhost:8000/mywatchlist ```,  kita perlu menambahkan perintah berikut pada variabel ```urlpatterns``` di urls.py yang terletak pada folder ```project_django```.
```
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

### Membuat sebuah model MyWatchList ###
Kemudian kita ingin membuat model ```MyWatchList``` dengan atribut sesuai dengan yang diinginkan, sehingga bentuk kode yang ditambahkan ke dalam views.py adalah:
```
from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
```

### Menambahkan minimal 10 data untuk objek MyWatchList ###
Selanjutnya di bagian menambahkan minimal 10 data untuk object MyWatchList, kita perlu membuat folder ```fixtures``` kemudian di dalamnya kita buat file .json dengan nama apapun (di kasus saya, saya beri nama initial_mywatchlist_data) dan menambahkan data dari setiap object yang ingin kita tambahkan. Contoh salah satu dari 10 data yang saya masukkan:
```
[
    {
        "model": "mywatchlist.listoffilm",
        "pk": 1,
        "fields": {
            "watched": true,
            "title": "How to Train Your Dragon",
            "rating": 5.00,
            "release_date": "2010-03-20",
            "review": "The story is so-so, but the animation is delicious."
        }
    },
    {
        ...
```
Lalu kita melakukan hal di atas untuk 10 data lainnya dengan isi dari setiap variabel yang berbeda

### Pengimplementasian fitur dalam tiga format ###
Pengimplementasian fitur untuk menyajikan data dalam format HTML:
menambahkan perintah di bawah pada file views.py
```
def show_my_watch_list(request):
    return render(request, "mywatchlist.html", context)

context = {
    'list_film': data_film,
    'namaku': 'Valencius Apriady Primayudha',
    'idku': '2106750830',
}
```

Untuk mengimplementasikan fitur data dengan format XML dan JSON, diperlukan mengimport hal berikut pada file views.py:
```
from django.http import HttpResponse
from django.core import serializers
```

Pengimplementasian fitur untuk menyajikan data dalam format XML:
menambahkan perintah di bawah pada file views.py
```
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Pengimplementasian fitur untuk menyajikan data dalam format JSON:
menambahkan perintah di bawah pada file views.py
```
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing dari fitur di atas ###
Selanjutnya, membuat routing sehingga data di atas dapat diakses melalui URL:
menambahkan perintah berikut pada utls.py 
```
    ...
    path('html/', show_my_watch_list, name='show_my_watch_list'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ...
```

### Deploy ke heroku ###
Dan yang terakhir untuk mendeploy heroku kita perlu menambahkan menambahkan data dari file json yang sudah kita buat tadi. Hal tersebut dengan menambahkan perintah ```&& python manage.py loaddata initial_mywatchlist_data.json``` pada file ```Procfile``` yang kita miliki. Terakhir tentunya kita perlu melakukan add commit push ke repository kita.

### Screenshot hasil pengaksesan ketiga url di atas dengan Postman ###
Berikut merupakan hasil screenshot dari pengaksesan 3 url di atas melalui postman:
HTML url:
![html1](https://user-images.githubusercontent.com/112455892/191641880-52ba1141-4361-4866-9c23-f2a3ade4498a.jpg)
XML url:
![xml](https://user-images.githubusercontent.com/112455892/191641914-352bd408-e061-4be5-b4de-4b5fb5ae49d0.jpg)
JSON url:
![json](https://user-images.githubusercontent.com/112455892/191641962-0972c11f-3462-41e8-b0c1-e47c42f03ad8.jpg)


