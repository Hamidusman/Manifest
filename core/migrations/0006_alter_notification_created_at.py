# Generated by Django 5.0 on 2023-12-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_rename_time_notification_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]