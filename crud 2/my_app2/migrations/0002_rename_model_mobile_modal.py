# Generated by Django 5.1.1 on 2024-09-24 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='model',
            new_name='modal',
        ),
    ]