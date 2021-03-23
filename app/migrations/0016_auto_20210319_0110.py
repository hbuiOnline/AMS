# Generated by Django 3.1.4 on 2021-03-19 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_auto_20210319_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-profile.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]