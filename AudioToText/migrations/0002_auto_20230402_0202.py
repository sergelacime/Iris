# Generated by Django 3.2.12 on 2023-04-02 02:02

import AudioToText.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioToText', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'verbose_name_plural': 'Audio'},
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=AudioToText.models.RenamedAudioFileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='audio',
            name='filename',
            field=models.CharField(default='audioIris', max_length=100),
        ),
    ]
