# Generated by Django 3.1.3 on 2020-12-12 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('antiplag', '0005_auto_20201212_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='antiplag.document'),
        ),
        migrations.AlterField(
            model_name='result',
            name='error_msg',
            field=models.TextField(null=True),
        ),
    ]
