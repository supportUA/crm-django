from django.contrib import admin
from .models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'pub_date', 'created_date')
    search_fields = ('name', 'email', 'phone')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'clients', 'pub_date', 'created_date')
    search_fields = ('name',)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_project', 'pub_date', 'created_date')
    search_fields = ('name', 'main_project', 'domain_d', 'server_d', 'bd_d', 'admin_panel')


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_todo', 'status', 'done', 'pub_date', 'created_date')
    search_fields = ('name', 'project_todo')


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Status)

