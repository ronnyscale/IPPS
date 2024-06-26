# Generated by Django 4.2.11 on 2024-06-13 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_academiccouncil_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academiccouncil',
            options={'verbose_name': 'Ученый совет', 'verbose_name_plural': 'Ученый совет'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['course'], 'verbose_name': 'Расписание ПА/ПЕРЕСДАЧ', 'verbose_name_plural': 'Расписания ПА/ПЕРЕСДАЧ'},
        ),
        migrations.AlterModelOptions(
            name='youthdivision',
            options={'verbose_name': 'Молодежный отдел', 'verbose_name_plural': 'Молодежные отделы'},
        ),
    ]
