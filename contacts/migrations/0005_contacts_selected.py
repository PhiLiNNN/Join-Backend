# Generated by Django 5.1.3 on 2025-01-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_tasks_assigned_to_tasks_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]