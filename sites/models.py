from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class Clients(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.CharField(max_length=200, verbose_name='Email')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    sites = models.ForeignKey('Site', on_delete=models.SET_NULL, related_name="clients", blank=True, null=True,
                              verbose_name='Сайт')
    notes = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Заметки о клиенте')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название проекта')
    clients = models.ForeignKey('Clients', on_delete=models.SET_NULL, related_name="clients", blank=True, null=True,
                                verbose_name='Клиент')
    history = models.TextField(max_length=3000, null=True, blank=True, verbose_name='История проекта')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.URLField(max_length=250, verbose_name='Ссылка на сайт')
    main_project = models.ForeignKey('Project', null=True, on_delete=models.SET_NULL, related_name="sites",
                                     verbose_name='Проект')
    domain_d = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Доступы к регистратору')
    server_d = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Доступ к серверу')
    bd_d = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Доступ к базе')
    admin_panel = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Админка')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Сайты'
        verbose_name = 'Сайт'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=3000, verbose_name='Название')
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name_plural = 'Статусы задач'
        verbose_name = 'Статусы задач'

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=3000, verbose_name='Задача')
    project_todo = models.ForeignKey('Project', null=True, on_delete=models.SET_NULL, verbose_name='Проект')
    content = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание задачи')
    status = models.ForeignKey('Status', null=True, on_delete=models.SET_NULL, verbose_name='Статус')
    done = models.BooleanField(verbose_name='Метка о выполнении')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
