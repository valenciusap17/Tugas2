# Tugas 2 PBP #

Situs heroku dapat diakses di [sini](https://tugas2pbp-valencius.herokuapp.com/katalog/)

## Bagan Request Client ke Web Aplikasi Berbasis Django ##

![pbp](https://user-images.githubusercontent.com/112455892/190127974-7b02e92f-62e2-4ed2-b909-6bd2c194b01e.jpg)

## Mengapa Menggunakan Virtual Environment ##

Fungsi dari virtual environment adalah agar kita dapat mengerjakan suatu project dengan menginstall berbagai package dan mengatur berbagai pengaturan tanpa mempengaruhi project lain yang berada di luar virtual environment yang kita buat. Kita dapat mengibaratkan virtual environment sebagai sebuah ruang lingkup kerja yang mana semua pengaturan dan packages yang kita install hanya khusus untuk project dalam ruang tersebut. 

Jika kita tidak menggunakan virtual environment kita memang masih dapat membuat aplikasi web berbasis Django, tetapi hal tersebut sangat rawan untuk mengakibatkan kekacauan jika kita sedang mengerjakan beberapa project yang membutuhkan pengaturan dan package yang berbeda sehingga kita tidak disarankan untuk tidak menggunakan virtual environment ketika kita sedang membuat aplikasi berbasis web.

## Cara Pengimplementasian ##
### Langkah 1: ###
Implemetasi kode:
```
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
```
Pertama-tama kita mengambil fungsi render dari library yang sudah disediakan, yaitu django.shortcuts, dan mengambil class CatalogItem dari models.py di folder katalog. Kemudian kita membuat sebuah fucntion yang diberi nama show_katalog dengan isi function render. Function render ini berfungsi untuk menggabungkan template (file .html) dengan dictionary context dan mengembalikan keduanya dalam bentuk object HttpResponse. Kemudian kita membuat variabel data_barang_katalog yang berisi seluruh object yang ada di dalam calss CatalogItem. Barulah pada akhirnya context tersebut diisi dengan properties yang diassign dengan variabel data_barang_katalog tadi, 'Valencius Apriady Primayudha', dan '2106750830' seperti yang dapat dilihat di atas.

### Langkah 2: ###
Implemetasi kode:
```
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/',include('katalog.urls')),
]
```
pada file urls.py di folder project_django kita menambahkan path('katalog/', include('katalog.urls')), yang berarti django akan mencari dan memotong url 'katalog/' dan akan lanjut menuju file yang ada di dalam include, yaitu file urls.py dalam folder katalog. 

implemetasi kode:
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'), 
]
```

kemudian pada file urls.py dalam folder katalog kita buat variabel urlpatterns yang diisi dengan path('', show_katalog, name='show_katalog'), yang berarti django akan mencari url kosong atau '' dan ketika menemukan url kosong akan lanjut ke function yang menjadi parameter selanjutnya, dalam aksus ini adalah show_katalog. shot_katalog sendiri kita dapatkan dengan mengimport dari views.py yang ada di dalam folder katalog.

### Langkah 3: ###
Menjalankan perintah python ```manage.py makemigrations``` untuk membuat migrasi skema model ke dalam database Django lokal. Selanjutnya melaksanakan perintah ```python manage.py migrate``` untuk menerapkan skema model yang tadi sudah dibuat. Kemudian menjalankan ```python manage.py loaddata initial_wishlist_data.json``` untuk memasukkan data-data yang sudah kita tulis di dalam file .json ke dalam database lokal django. 



Pada file template html yang sudah ada, kita perlu memanfaatkan penggunaan double curly braces {{}} untuk mengoper nilai variabel python ke dalam file html seperti pada kode di bawah:
```
  <p>{{ namaku }} </p>
```
Kode di atas akan mengembalikan value dari variabel python ``` namaku ``` yaitu "Valencius Apriady Primayudha. ```namaku``` sendiri berasal dari properties yang dibuat pada context yang digabung dengan file .html pada saat kita menggunakan melaksanaan function render di views.py.

### Langkah 4: ###
Untuk melakukan deploy pada aplikasi heroku, kita memerlukan file ```Procfile```, file ```dpl.yml```, dan menambahkan ```HEROKU_API_KEY``` dan ```HEROKU_APP_NAME``` pada secrets repository github.
