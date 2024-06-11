# Generated by Django 4.2.11 on 2024-06-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='assessment_type',
            field=models.CharField(choices=[('exam', 'Экзамен'), ('credit', 'Зачет')], default='', max_length=10, verbose_name='Тип проведения'),
            preserve_default=False,
        ),
    ]
