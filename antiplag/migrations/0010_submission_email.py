# Generated by Django 3.1.3 on 2021-03-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("antiplag", "0009_auto_20201213_1555"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
