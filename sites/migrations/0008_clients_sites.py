# Generated by Django 3.0.3 on 2020-03-03 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0007_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='sites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='sites.Site', verbose_name='Сайт'),
        ),
    ]
