# Tugas 4 PBP #

Link heroku dapat diakses [disini](https://tugas2pbp-valencius.herokuapp.com/todolist/)

2 Akun pengguna yang sudah dibuat:

1.  Username: dummy1
    
    Password: tesbenar

2.  Username: dummy2
    
    Password: tesbenar

## Kegunaan ```{% csrf_token %}``` pada elemen ```<form>``` dan apa yang terjadi jika kita tidak memakainya ##

CSRF adalah singkatan dari Cross-site Request Forgery yang merupakan kerentanan sekuritas website yang dapat mengizinkan orang lain untuk memanipulasi pengguna untuk melakukan tindakan yang sebenarnya tidak mereka lakukan. 

```{% csrf_token %}``` adalah sebuah tag yang dimiliki oleh django dengan fungsi untuk menghindar dari serangan-serangan berbahaya. Tag tersebut akan menghasilkan sebuah token untuk sisi server ketika kita melakukan render pada form. Hal tersebut menyebabkan setiap kali kita mengirimkan request, maka server akan mengecek apakah token request yang dikirimkan sesuai dengan token yang dihasilkan tadi oleh tag ```{% csrf_token %}```. Jika tidak sesuai, maka perintah dari request tersebut tidak akan dieksekusi. Jika kita tidak menggunakan ```{% csrf_token %}```, sesuai dengan yang sempat dibahas tadi, maka form yang kita miliki akan rentan dengan serangan-serangan CSRF.

## Cara membuat element ```<form>``` secara manual ##

Kita BISA menambahkan element ```<form>``` secara manual. Caranya adalah dengan membuat folder fixtures dan menambahkan file json di dalamnya. Di dalam file json tersebut berisi data-data yang ingin kita masukkan secara manual ke dalam form. Maka data tersebut akan diakses melalui file html dengan menggunakan variabel ```name``` yang mana value dari variabel tersebut akan diteruskan ke html tersebut. Contoh:

salah satu data dalam file json:
```
    {
        "name": "Valencius Apriady Primayudha"
        ...
    }
```

Maka pengakses data dalam file html:
```
<input type="text" name="task"/>
```

## Proses alur data ##

Awalnya tentu user atau pengguna mengisi form tempat menampung data yang akan diproses. Kemudian data tersebut akan diproses sesuai dengan perintah kode yang disertakan pada pembuatan form. Lalu data tersebut akan disimpan di dalam database jika semua prasyarat (penggunaan method yang benar, parameter yang diberikan sudah sesuai, dll) sudah terpenuhi. Kemudian data yang sudah ada di dalam databse dapat kita akses melalui ```views.py```. Kita perlu membuat function yang isinya adalah melakukan render file template html yang sudah ada beserta dengan data yang diinginkan.

## Cara mengimplementasikan checklist di atas ##

### Membuat aplikasi baru bernama todolist ###
Pertama-tama, kita akan membuat suatu aplikasi baru dengan nama todolist di proyek Tugas 2 pekan lalu. Maka, kita harus change directory kita pada terminal yang kita gunakan menuju folder Tugas2 yang sudah kita miliki sejak pekan-pekan lalu. Sebelum kita masuk ke dalam pengimplementasian, kita perlu menyalakan virtual environment terlebih dahulu dengan menjalankan perintah:
```
python -m venv env
env\Scripts\activate.bat
```
Kemudian untuk membuat aplikasi baru kita menjalankan perintah :
```
python manage.py startapp todolist
```

### Menambahkan path todolist ###
Untuk checklist selanjutnya, agar kita bisa mengakses ``` http://localhost:8000/todolist ```,  kita perlu menambahkan perintah berikut pada variabel ```urlpatterns``` di urls.py yang terletak pada folder ```project_django```.
```
    ...
    path('todolist/', include('todolist.urls')),
]
```

### Membuat sebuah model Task ###
Kemudian kita ingin membuat model ```Task``` dengan atribut sesuai dengan yang diinginkan, sehingga bentuk kode yang ditambahkan ke dalam views.py adalah:
```
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
```

### Mengimplementasikan form registrasi, login, dan logout ###
Untuk implementasi ini kita perlu mengedit beberapa file:

Kode yang ditambahkan pada file ```views.py```:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response 
```
Kode-kode diatas kita tambahkan untuk mengambil data yang kita perlukan dari database dan kemudian kita render file template html yang sudah ada disertai dengan data yang sempat kita ambil tadi.


Lalu kita juga perlu membuat file html sebagai template yang akan menghasilkan tampilan yang kita dapat kita lihat nantinya di website kita. File html yang perlu kita buat adalah:

```login.html``` yang berisikan kode sebagai berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```

```register.html``` yang berisikan kode sebagai berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

### Membuat halaman todolist beserta dengan komponen yang harus ada di dalamnya ###
Halaman todolist ini berarti kita ingin membuat file template html yang isinya adalah kode untuk menampilkan seluruh komponen yang kita inginkan. Kode yang saya sisipkan untuk melakukan hal diatas sebagai berikut:
```
{% extends 'base.html' %}

 {% block content %}

 {% load static %}

  <h1>Tugas 4 Assignment PBP/PBD</h1>

  <span><h5></h5><b>Name: </b>{{nama}} </span>
  <p></p>

  <table>
    <tr>
      <th>Task Title</th>
      <th>Task Date</th>
      <th>Task Description</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for task in list_task %}
      <tr>
        <th>{{task.title}}</th>
        <th>{{task.date}}</th>
        <th>{{task.description}}</th>
      </tr>
    {% endfor %}
  </table>
  <h5>Sesi terakhir login: {{ last_login }}</h5>
  <button><a href="{% url 'todolist:create_task' %}">Create Task</a></button>

  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

 {% endblock content %}
```
Setelah itu tentunya kita perlu membuat function untuk menampilkan todolist yang kita miliki. Hal tersebut dapat kita lakukan membuat function show_todolist di dalam ```views.py``` yang berisikan kode sebagai berikut:
```
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.all()
    context = {
        'list_task': data_task,
        'nama': request.user,
        'last_login': request.COOKIES['last_login'],
        
    }
    return render(request, 'todolist.html', context)    
```

### Membuat halaman form untuk membuat task ###
Untuk membuat halaman form maka saya menggunakan cara membuat sebuah file template html yang akan menjadi tampilan form nanti. File template html tersebut akan berisi kode sebagai berikut:
```
<html>
<head>
<title>Create Task</title>
</head>

<body>
<h1>Create Your new Task </h1>
<form action="" method="POST">
{% csrf_token %}
Title Task: <input type="text" name="task"/><br/>
Description Content: <br/>
<textarea cols="35" rows="8" name="desc">
</textarea><br/>
<input type="submit" value="Create new Task"/>
</form>
</body>

</html>
```
Setelah itu kita juga harus membuat sebuah function di ```views.py``` yang memiliki fungsi untuk mengambil data yang tertera di dalam form (dari user) untuk kita masukkan ke dalam database. Kodenya sebagai berikut:
```
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user = request.user, 
            date = timezone.now(), 
            title = request.POST.get("task"), 
            description = request.POST.get("desc"),
        )
        return HttpResponseRedirect(reverse('todolist:show_todolist'))

    return render(request, 'create_task.html', {})
```

### Membuat router ke berbagai fungsi ###
Perlakuan routing tersebut kita aplikasikan dengan menambahkan kode pada ```urls.py``` seperti berikut:
```
from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

## Deploy ke Heroku ##
Pada akhirnya tentu yang perlu kita lakukan adalah push ke github dan akan secara otomatis akan deploy ke heroku.