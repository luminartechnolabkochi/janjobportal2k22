# Generated by Django 3.2.12 on 2022-05-17 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='job_title',
            new_name='job_title_name',
        ),
    ]
