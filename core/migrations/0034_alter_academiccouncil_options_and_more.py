# Generated by Django 4.2.11 on 2024-06-13 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_person_password_person_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academiccouncil',
            options={'verbose_name': 'Ученый совет'},
        ),
        migrations.AlterModelOptions(
            name='academictitle',
            options={'verbose_name': 'Учёное звание', 'verbose_name_plural': 'Учёные звания'},
        ),
        migrations.AlterModelOptions(
            name='additionaleducationprogram',
            options={'verbose_name': 'Дополнительное образование'},
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Кафедра', 'verbose_name_plural': 'Кафедры'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Партнер', 'verbose_name_plural': 'Партнеры'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Пользователь сайта', 'verbose_name_plural': 'Пользователи сайта'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='presentation',
            options={'verbose_name': 'Презентация', 'verbose_name_plural': 'Презентации'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['course'], 'verbose_name': 'Расписание ПА/ПЕРЕСДАЧ'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterModelOptions(
            name='studentlifeevent',
            options={'verbose_name': 'Мероприятие студенческой жизни', 'verbose_name_plural': 'Мероприятия студенческой жизни'},
        ),
        migrations.AlterModelOptions(
            name='youthdivision',
            options={'verbose_name': 'Молодежный отдел'},
        ),
    ]