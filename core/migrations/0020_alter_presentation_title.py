# Generated by Django 4.2.11 on 2024-06-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_presentation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок презентации'),
        ),
    ]