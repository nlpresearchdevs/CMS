# Generated by Django 2.1.4 on 2019-01-07 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0006_auto_20190107_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='resWatsonSentiment',
            new_name='resWatsonSentiments',
        ),
    ]
