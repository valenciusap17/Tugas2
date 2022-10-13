# Tugas 6 PBP #

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming ##
Proses jalannya program pada asynchronus programming bisa berjalan secara bersamaan tanpa harus menunggu proses antrian. Synchronus programming sendiri merupakan bagian Asynchronus programming, berupa 1 antrian, yang mana proses eksekusinya akan dilaksanakan secara bersamaan dan untuk hasilnya tergantung durasi proses suatu fungsi synchronus.

## Maksud dari event-driven programming dan salah satu contohnya ##
Event-driven programing adalah suatu paradigma pemrograman yang alur jalannya pemrograman bergantung dengan keluaran/output hasil tindakan yang dilakukan oleh user. Contohnya adalah ketika terdapat dua tombol, tombol pertama berlabelkan "Main menu" dan tombol yang kedua berlabel kan "logout". Jika user memilih dan memencet tombol "Main menu", maka output keluaran yang akan dihasilkan adalah halaman akan berpindah ke halaman utama (main menu), sedangkan ketika kita memencet tombol logout keluaran event yang akan dihasilkan adalah user akan terlogout dan perlu melakukan sign in ke dalam akun yang ia miliki untuk kembali mengakses akun user.

## Penerapan Asynchronus Programming pada AJAX ##
Dengan menggunakan AJAX dan menerapkan asyncrhonus programming, jalannya program sudah tidak bergantung dengan proses urutan proses yang harusnya dijalankan. AJAX dapat langsung mengambil data-data yang baru saja di dapatkan tanpa merefresh halaman tempat pengambilan data sehingga semuanay dilakukan di belakang layar. Hal ini menyebabkan ketika kita menggunakana AJAX kita tidak perlu mereload halaman bila terdapat penambahan atau pengurangan data dalam skala yang tidak terlalu besar.

## Cara Mengimplementasikan Checklist di Atas ##

Pertama-tama kita ingin menampilkan selueuh data task dalam bentuk JSON, maka kita perlu menampahkan parh url baru ke dalam urls.py dan membuat function untuk menampilkan data pada file json tersebut. Berikut merupakan potongan kodenya 
Menambahkan kode berikut pada urls.py:
```
...
    path('json/', get_todolist_json, name='get_todolist_json'),
...
```

Menambahkan kode berikut pada views.py:
```
...
def get_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data))
...
```

Setelah kita menampilkan data dalam bentuk json maka sekarang kita mulai mengimplementasikan AJAX yang kita inginkan. kita membuat tag script yang isinya berfungsi untuk melakukan import jquery AJAX. 

Pertama-tama saya membuat sebuah container kosong yang nantinya akan diisi oleh konten todolist sama seperti tugas pekan lalu. Impemetasi kode sebagai berikut:
```
<div class="container">
  <div id="containCards">

  </div>
</div>
```

Kemudian kita akan membuat sebuah tampilan pop out berupa form yang berguna untuk mengambil input user yang kemudian akan kita proses di dalam tag script yang kita miliki. Untuk mengaplikasikannya, saya menggunakan modal yang dimiliki oleh bootstrep. implementasi kodenya sebagai berikut:
```
<div class="flex-second">
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Create Task</button>
</div>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Create Your New Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="formnewtask">
          {% csrf_token %}
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Title</label>
            <input type="text" class="form-control" id="title" name ="title">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Description</label>
            <textarea class="form-control" id="description" name="description"></textarea>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="taskbutton"  data-bs-dismiss="modal">Save New Task</button>
      </div>
    </div>
  </div>
</div>
```

Setelah itu, kita membuat sebuah function document.ready yang fungsinya adalah merender data yang ada. Implementasi kode sebagai berikut:
```
$(document).ready(function(){
    refreshTodolist();
  });
```

Kemudian kita function asyncrhonus yang berfungsi untuk mengambil semua data dari json yang tadi sudah kita buat. Maka kita menggunakan function fetch yang akan mengambil data dengan function ```get_todolist_json``` pada views.py. Implementasinya sebagai berikut:
```
async function getTodolist() {
    return fetch("{% url 'todolist:get_todolist_json' %}").then((res) => res.json())
  }
```

Selanjutnya adalah membuat function rerfreshtodolist yang inti isinya adalah kita mengisi container kosong yang tadi sempat kita isi dengan konten sesuai dengan desain container yang sempat kita buat pada tugas sebelumnya. Selain itu ada juga function addTodoList yang isinya melakukan fetch dari function add_todolist_item yang ada di views.py untuk mengambil data-data json yang ada dan kemudian menggunakan method "POST" yang berfungsi untuk memasukka data-data yang akan diambil dari input user pada modal yang sudah sempat kita buat. implementasi kode sebagai berikut:
```
async function refreshTodolist() {
        document.getElementById("containCards").innerHTML = ""
        const todolist = await getTodolist()
        let htmlString = ``
        todolist.forEach((item) => {
          htmlString += `\n
          <tr>
            <div class="flex-first">
              <div class="cards">
                <div class="p-6 max-w-sm bg-white rounded-lg border border-gray-800 shadow-md dark:bg-gray-800 dark:border-gray-700 card text-center">
                    <div class="flex-first">
                      <h1 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${item.fields.title}</h1>
                      {% if task.is_finished %} <h1>&#9989;</h1> {% else %} <h1>&#10060;</h1> {% endif %}
                    </div>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">${item.fields.description}</p>
                    <h6>${item.fields.date}</h6>
                </div>
              </div>
            </div>
          </tr>
          ` 
        })
        
        document.getElementById("containCards").innerHTML = htmlString
  }

  function addTodolist() {
    fetch("{% url 'todolist:add_todolist_item' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#formnewtask'))
      }).then(refreshTodolist)
    return false
  }
  document.getElementById("taskbutton").onclick = addTodolist
  refreshTodolist()
```

Setelah semua selesai, maka kita melakukan git add, commit, push untuk gitub yang kita miliki