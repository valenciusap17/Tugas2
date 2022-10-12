from django.urls import path
from todolist.views import deleting_task, register, login_user, logout_user, show_todolist, create_task, converting_status, deleting_task, get_todolist_json
from todolist.views import add_todolist_item
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('converting-status/<int:id>', converting_status, name='converting_status'),
    path('delete-task/<int:id>', deleting_task, name='deleting_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add_todolist_item', add_todolist_item, name="add_todolist_item"),
]