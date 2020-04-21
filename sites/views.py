from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProjectForm, SiteForm, ClientForm, TodosForm


def index(request):
    # Главная страница
    projects = Project.objects.order_by("-id")[0:3]
    sites = Site.objects.order_by("-id")[0:3]
    todos = Todo.objects.order_by("-id")[0:10]
    clients = Clients.objects.order_by("-id")[0:3]
    all_project = Project.objects.all().count()
    all_sites = Site.objects.all().count()
    all_todo = Todo.objects.all().count()
    all_clients = Clients.objects.all().count()
    context = {'projects': projects, 'clients': clients, 'sites':sites, 'todos': todos, 'all_project': all_project,
               'all_sites': all_sites, 'all_todo': all_todo, 'all_clients': all_clients}
    return render(request, 'crm/home.html', context)


def projects_list(request):
    # Страница проектов
    clients = Clients.objects.all()
    projects = Project.objects.all()
    return render(request, 'crm/project_list.html', context={'projects': projects, 'clients': clients})


def client_detail(request, clients_id):
    # Страница одного клиента
    client = get_object_or_404(Clients, pk=clients_id)
    return render(request, 'crm/client_detail.html', {'client': client})


def site_detail(request, site_id):
    # Страница одного сайта
    projects = Project.objects.all()
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'crm/site_detail.html', {'site': site, 'projects': projects})


def project_detail(request, project_id):
    # Страница одного проекта
    todos = Todo.objects.filter(project_todo=project_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'crm/project_detail.html', {'project': project, 'todos': todos})


def todo_detail(request, todo_id):
    # Страница одного проекта
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'crm/todo_detail.html', {'todo': todo})



def clients_list(request):
    # Страница клиентов
    clients = Clients.objects.all()
    return render(request, 'crm/clients_list.html', context={'clients': clients})


def sites_list(request):
    # Страница сайтов
    sites = Site.objects.all()
    return render(request, 'crm/sites_list.html', context={'sites': sites})


def todos_list(request):
    # Страница со списком всех задач
    projects = Project.objects.all()
    todos = Todo.objects.all()
    return render(request, 'crm/todos_list.html', context={'todos': todos, 'projects': projects})


def create_project(request):
    # Функция создать проект
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    context = {'form': form}
    return render(request, 'crm/forms/create.html', context)


def update_project(request, pk):
    # Функция обновить проект
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    context = {"form": form}
    return render(request, 'crm/forms/create.html', context)


def delete_project(request, pk):
    # Функция удалить проект
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('/projects/')
    context = {'item':project}
    return render(request, 'crm/forms/delete_project.html', context)


def create_site(request):
    # Функция создать сайт
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sites/')
    context = {'form': form}
    return render(request, 'crm/forms/create.html', context)


def update_site(request, pk):
    # Функция обновить сайт
    site = Site.objects.get(id=pk)
    form = SiteForm(instance=site)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('/sites/')
    context = {"form": form}
    return render(request, 'crm/forms/create.html', context)


def delete_site(request, pk):
    # Функция удалить сайт
    site = Site.objects.get(id=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('/sites/')
    context = {'item':site}
    return render(request, 'crm/forms/delete_site.html', context)


def create_client(request):
    # Функция создать клиента
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients/')
    context = {'form': form}
    return render(request, 'crm/forms/create.html', context)


def update_client(request, pk):
    # Функция обновить данные клиента
    client = Clients.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clients/')
    context = {"form": form}
    return render(request, 'crm/forms/create.html', context)


def delete_client(request, pk):
    # Функция удалить клиента
    client = Clients.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/clients/')
    context = {'item':client}
    return render(request, 'crm/forms/delete_client.html', context)


def create_todos(request):
    # Функция создать клиента
    form = TodosForm()
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    context = {'form': form}
    return render(request, 'crm/forms/create.html', context)


def update_todos(request, pk):
    # Функция обновить данные клиента
    todo = Todo.objects.get(id=pk)
    form = TodosForm(instance=todo)
    if request.method == 'POST':
        form = TodosForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    context = {"form": form}
    return render(request, 'crm/forms/create.html', context)


def delete_todos(request, pk):
    # Функция удалить клиента
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/todos/')
    context = {'item':todo}
    return render(request, 'crm/forms/delete_todos.html', context)


def todos_off(request, pk):
    # Метка о выполнении (Выполненно)
    todo = Todo.objects.get(id=pk)
    todo.done = True
    todo.save()
    return redirect('/todos/')


def todos_on(request, pk):
    # Метка о выполнении (не выполненно)
    todo = Todo.objects.get(id=pk)
    todo.done = False
    todo.save()
    return redirect('/todos/')