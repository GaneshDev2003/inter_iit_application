# Generated by Django 4.0.5 on 2022-12-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burst_finder', '0002_rename_dateuploaded_xraydatamodel_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='xraydatamodel',
            name='plot_data',
            field=models.CharField(default='', max_length=1000),
        ),
    ]