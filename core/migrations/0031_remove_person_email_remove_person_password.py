# Generated by Django 4.2.11 on 2024-06-13 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_person_password_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
    ]