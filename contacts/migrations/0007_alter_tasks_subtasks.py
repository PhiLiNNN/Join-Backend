# Generated by Django 5.1.3 on 2025-01-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_tasks_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='subtasks',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]