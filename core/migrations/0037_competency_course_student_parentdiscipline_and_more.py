# Generated by Django 4.2.11 on 2024-06-19 09:55

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_additionaleducationprogram_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('code', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, populate_from='slugify_function', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='core.course')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='ParentDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_disciplines', to='core.course')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, populate_from='slugify_function', unique=True)),
                ('competencies', models.ManyToManyField(related_name='disciplines', to='core.competency')),
                ('parent_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', to='core.parentdiscipline')),
            ],
        ),
    ]