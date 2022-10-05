# Tugas 5 PBP #

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? ##
Eksternal CSS adalah kode CSS yang ditulis di file khusus dengan format file .css sehingga penulisannya terpisah dengan kode HTML. Beberapa kelebihan yang dimiliki ketika kita menggunakan eksternal CSS adalah kode penulisan dalam file HTML yang kita miliki menjadi lebih pendek, penulisan struktur kode lebih rapih , dan bisa dipakai oleh file lainnya juga. Kekurangan yang dimiliki oleh eksternal CSS adalah ketergantungan file HTML terhadap file CSS eksternal sehingga jika file CSS gagal dipanggil oleh file HTML itu sendiri, maka tampilan halaman akan berantakan. Biasanya terjadi karena koneksi internet yang lambat.

contoh yang dimiliki eksternal CSS adalah:
```
i {
    font-family: arial;
    color: orange;
}
```

Inline CSS adalah kode yang dituliskan secara langsung kepada bagian style dari setiap elemen HTML. Penggunaan Inline CSS ini cenderung kurang efisien karena kita harus mengubah style dari setiap tag HTML satu per satu. Tetapi penggunaan Inline CSS cukup membantu ketika kita sedang menguji style yang diberikan pada suatu elemen. Hal tersebut juga membantu kita agar waktu yang digunakan untuk memperbaiki kode menjadi lebih sedikit. Proses load webiste juga menjadi lebih cepat dan proses permintaan HTTP lebih kecil.

contoh yang dimiliki inline CSS adalah:
```
<h1 style="color:blue;">Valencius</h1>
```

Internal CSS adalah kode CSS yang ditulis di bagian dalam tag ```<style>``` dan bagian header file HTML. Hal ini bertujuan agar perubahan kode pada satu file tidak akan merubah tampilan dari kode lain. Hal ini membuat tampilan dari setiap kode berbeda akan bersifat unik. Kita sudah tidak perlu menambahkan file HTML dan CSS ke dalam satu folder bersama lagi. Meskipun begitu, internal CSS kurang efisien jika ternyata kode CSS yang ditambahkan pada kode lain sama. kode CSS yang berbeda-beda juga akan membuat performa website menjadi lebih lambat.

contoh yang dimiliki internal CSS adlaah:
```
...
   <style>
    .flex-first {
      font-size: 250%;
    }
  </style>
...
```

## Tag HTML5 yang Diketahui ##
```<form>``` = blok yang menyatakan form untuk input user

```<head>``` = blok yang menyatakan bagian kepala dari sebuah kode atau dokumen

```<img>``` = blok yang mewakili sebuah gambar

```<input>``` = blok untuk mentrol input

```<link>``` = blok untuk mendefinisikan hubungan antara sumber dari luar dengan dokumen atau kode saat ini

```<p>``` = blok yang menyatakan sebuah paragraf

```<div>``` = blok yang meenegaskan sebuah bagian atau sektor dari dokumen atau kode
dan lain-lain

## Tipe CSS Selector yang Diketahui ##
```.class``` = mengambil semua elemen dalam class yang dirujuk
```*``` = mengambil semua elemen
```[attribute]``` = mengambil elemen dengan atribut yang dirujuk
```:active``` = memiliki link yang aktif
dan lain-lain

## Cara Mengimplementasikan Kode yang Sudah Dibuat ##
Pertama-tama kita mengambil CDN dari bootstrap, flowbite, dan CSS ke dalam file ```base.html``` di folder templates yang kita miliki. Kemudian saya membaca berbagai docs dari semua CDN yang sudah sempat saya masukkan. Kemudian saya mengimplementasikan sesuai dengan kreasi yang saya inginkan dan penggunaan cards untuk halaman utama todolist. Setelah itu tentunya mencoba melihat hasil setelah kode selesai diedit sambil melakukan debug untuk mendapatkan hasil yang saya inginkan. Setelah semua tampilan sudah sesuai dengan yang kita inginkan, maka kita melakukan git add, commit, dan push ke github yang kemudian secara otomatis akan terdeploy ke heroku.