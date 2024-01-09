# Generated by Django 4.2.8 on 2024-01-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="about",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile-pic"),
        ),
    ]
