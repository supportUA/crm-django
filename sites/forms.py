from django.forms import ModelForm
from .models import Project, Site, Clients, Todo


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'


class TodosForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
