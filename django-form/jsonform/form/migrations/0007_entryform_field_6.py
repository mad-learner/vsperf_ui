# Generated by Django 3.0.4 on 2020-04-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20200405_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='entryform',
            name='field_6',
            field=models.CharField(default='', max_length=200),
        ),
    ]
