# Generated by Django 3.2.12 on 2023-04-07 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AudioToText', '0003_report_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='Report',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]