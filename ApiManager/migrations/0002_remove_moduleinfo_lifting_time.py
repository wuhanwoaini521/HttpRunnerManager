# Generated by Django 2.0.3 on 2018-04-21 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduleinfo',
            name='lifting_time',
        ),
    ]