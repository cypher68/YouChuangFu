# Generated by Django 4.2.15 on 2024-10-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="book",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=45)),
                ("password", models.CharField(max_length=45)),
            ],
        ),
        migrations.DeleteModel(
            name="UserInfo",
        ),
    ]
