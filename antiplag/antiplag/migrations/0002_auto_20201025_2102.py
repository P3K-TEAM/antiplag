# Generated by Django 3.1.2 on 2020-10-25 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("antiplag", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="text",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="papers/")),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="antiplag.paper"
                    ),
                ),
            ],
        ),
    ]
