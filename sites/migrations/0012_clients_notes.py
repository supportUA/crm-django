# Generated by Django 3.0.3 on 2020-03-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0011_auto_20200304_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Заметки о клиенте'),
        ),
    ]