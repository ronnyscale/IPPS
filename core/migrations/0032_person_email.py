# Generated by Django 4.2.11 on 2024-06-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_remove_person_email_remove_person_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
