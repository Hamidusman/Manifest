# Generated by Django 4.2.8 on 2023-12-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_remove_notification_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
