# Generated by Django 4.0.5 on 2022-12-15 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burst_finder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xraydatamodel',
            old_name='dateUploaded',
            new_name='date_uploaded',
        ),
        migrations.RenameField(
            model_name='xraydatamodel',
            old_name='fileName',
            new_name='file_name',
        ),
    ]
