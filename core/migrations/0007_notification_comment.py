# Generated by Django 5.0 on 2023-12-27 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_alter_notification_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="comment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.comment",
            ),
        ),
    ]