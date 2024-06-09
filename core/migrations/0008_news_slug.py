# Generated by Django 4.2.11 on 2024-06-07 04:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default=' ', editable=False, populate_from='slugify_function', unique=True),
        ),
    ]
