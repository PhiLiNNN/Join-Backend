# Generated by Django 5.1.3 on 2025-01-04 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_rename_title_tasks_titlee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='titlee',
            new_name='title',
        ),
    ]
