from multiprocessing import context
from time import time, timezone
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import todolist
from todolist.models import Task
import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core import serializers
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_task,
        'nama': request.user,
        'last_login': request.COOKIES['last_login'],
        
    }
    return render(request, 'todolist.html', context)


def get_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data))

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


def add_todolist_item(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task(user=request.user, date=timezone.now(), title=title, description=description, is_finished=False)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

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

@login_required(login_url='/todolist/login/')
def deleting_task(request, id):
    stuff = Task.objects.get(user=request.user, id = id)
    stuff.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def converting_status(request, id):
    stuff = Task.objects.get(user=request.user, id = id)    
    stuff.is_finished = not stuff.is_finished
    stuff.save(update_fields=["is_finished"])
    return redirect('todolist:show_todolist')