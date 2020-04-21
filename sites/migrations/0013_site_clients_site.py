# Generated by Django 3.0.3 on 2020-03-18 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0012_clients_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='clients_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_site', to='sites.Clients', verbose_name='Клиент'),
        ),
    ]
