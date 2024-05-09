# Generated by Django 5.0.6 on 2024-05-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WordCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(blank=True, max_length=250, null=True)),
                ("word", models.CharField(blank=True, max_length=100, null=True)),
                ("count", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]