# Generated by Django 4.2.6 on 2023-10-05 14:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo_app", "0004_alter_task_datetime_deadline"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_done", "-datetime_created_at"]},
        ),
    ]
