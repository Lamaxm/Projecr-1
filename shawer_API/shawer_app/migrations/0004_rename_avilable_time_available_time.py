# Generated by Django 4.0.4 on 2022-06-14 10:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shawer_app', '0003_avilable_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='avilable_time',
            new_name='available_time',
        ),
    ]