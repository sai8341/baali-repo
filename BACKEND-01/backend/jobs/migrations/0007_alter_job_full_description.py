# Generated by Django 5.1.4 on 2024-12-30 10:55

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_job_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='full_description',
            field=tinymce.models.HTMLField(help_text='Enter the Full Job Data'),
        ),
    ]
