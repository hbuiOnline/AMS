# Generated by Django 3.1.4 on 2021-03-03 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210302_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
