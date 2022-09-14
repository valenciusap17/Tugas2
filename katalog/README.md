# Bagan Request Client ke Web Aplikasi Berbasis Django #

![](pbp.jpg)


> Mengapa Menggunakan Virtual Environment

Fungsi dari virtual environment adalah agar kita dapat mengerjakan suatu project dengan menginstall berbagai package dan mengatur berbagai pengaturan tanpa mempengaruhi project lain yang berada di luar virtual environment yang kita buat. Kita dapat mengibaratkan virtual environment sebagai sebuah ruang lingkup kerja yang mana semua pengaturan dan packages yang kita install hanya khusus untuk project dalam ruang tersebut. 

Jika kita tidak menggunakan virtual environment kita memang masih dapat membuat aplikasi web berbasis Django, tetapi hal tersebut sangat rawan untuk mengakibatkan kekacauan jika kita sedang mengerjakan beberapa project yang membutuhkan pengaturan dan package yang berbeda sehingga kita tidak disarankan untuk tidak menggunakan virtual environment ketika kita sedang membuat aplikasi berbasis web.


>Cara Implementasi

## Langkah 1: ##
Implemetasi kode saya:

![](pbp.jpg)

Pertama-tama kita mengambil fungsi render dari library yang sudah disediakan, yaitu django.shortcuts, dan mengambil class CatalogItem dari models.py di folder katalog. Kemudian kita membuat sebuah fucntion yang diberi nama show_katalog dengan isi function render. Function render ini berfungsi untuk menggabungkan template dengan dictionary context dan mengembalikan keduanya dalam bentuk object HttpResponse. Kemudian kita membuat variabel data_barang_katalog yang berisi seluruh object yang ada di dalam calss CatalogItem. Barulah pada akhirnya context tersebut diisi dengan properties yang diassign dengan variabel data_barang_katalog tadi, nama saya, dan nomor identitas saya seperti yang dapat dilihat di atas.

## Langkah 2: ##
Implemetasi kode saya:
![](pbp.jpg)
pada file urls.py di folder project_django kita menambahkan path('katalog/', include('katalog.urls')), yang berarti django akan mencari dan memotong url 'katalog/' dan akan lanjut menuju file yang ada di dalam include, yaitu file urls.py dalam folder katalog. 

kemudian pada file urls.py dalam folder katalog kita buat variabel urlpatterns yang diisi dengan path('', show_katalog, name='show_katalog'), yang berarti django akan mencari url kosong atau '' dan ketika menemukan url kosong akan lanjut ke function yang menjadi parameter selanjutnya, dalam aksus ini adalah show_katalog. shot_katalog sendiri kita dapatkan dengan mengimport dari views.py yang ada di dalam folder katalog.

## Langkah 3: ##
Menjalankan perintah python manage.py makemigrations untuk membuat migrasi skema model ke dalam database Django lokal. Selanjutnya melaksanakan perintah python manage.py migrate untuk menerapkan sekma model yang tadi sudah dibuat. Kemudian menjalankan python manage.py loaddata initial_wishlist_data.json untuk memasukkan data-data yang sudah kita tulis di dalam file .json ke dalam database lokal django. 

Implementasi kode saya:
![](pbp.jpg)
Pada file template html yang sudah ada, kita perlu memanfaatkan penggunaan double curly braces {{}} untuk mengoper nilai variabel python ke dalam file html seperti pada gambar di atas.

## Langkah 4: ##
Untuk melakukan deploy pada aplikasi heroku, kita memerlukan file Procfile, file dpl.yml, dan menambahkan HEROKU_API_KEY dan HEROKU_APP_NAME pada secrets repository github.

