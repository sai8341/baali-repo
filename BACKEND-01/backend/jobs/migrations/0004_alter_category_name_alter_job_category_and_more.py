# Generated by Django 5.1.4 on 2024-12-30 07:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_category_job_count_alter_job_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='job',
            name='full_description',
            field=models.TextField(verbose_name='Full Description'),
        ),
        migrations.AlterField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Posted By'),
        ),
        migrations.AlterField(
            model_name='job',
            name='qualifications',
            field=models.TextField(verbose_name='Qualifications'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=50, verbose_name='Salary Range'),
        ),
    ]