from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('clients/', clients_list, name="clients_list"),
    path('projects/', projects_list, name="projects_list"),
    path('sites/', sites_list, name="sites_list"),
    path('todos/', todos_list, name="todos_list"),

    path('client/<int:clients_id>/', client_detail, name='client_detail'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('site/<int:site_id>/', site_detail, name='site_detail'),
    path('todo/<int:todo_id>/', todo_detail, name='todo_detail'),

    path('create-project/', create_project, name="create_project"),
    path('update-project/<str:pk>/', update_project, name="update_project"),
    path('delete-project/<str:pk>/', delete_project, name="delete_project"),

    path('create-site/', create_site, name="create_site"),
    path('update-site/<str:pk>/', update_site, name="update_site"),
    path('delete-site/<str:pk>/', delete_site, name="delete_site"),

    path('create-client/', create_client, name="create_client"),
    path('update-client/<str:pk>/', update_client, name="update_client"),
    path('delete-client/<str:pk>/', delete_client, name="delete_client"),

    path('create-todos/', create_todos, name="create_todos"),
    path('update-todos/<str:pk>/', update_todos, name="update_todos"),
    path('delete-todos/<str:pk>/', delete_todos, name="delete_todos"),
    path('todos-off/<str:pk>/', todos_off, name="todos_off"),
    path('todos-on/<str:pk>/', todos_on, name="todos_on"),
]