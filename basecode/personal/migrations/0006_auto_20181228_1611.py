# Generated by Django 2.1.4 on 2018-12-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20181228_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='resWatsonClase',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='resWatsonScore',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
