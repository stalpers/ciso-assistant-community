# Generated by Django 4.2.1 on 2023-07-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_requirementassessment_major_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='attachment',
            field=models.FileField(blank=True, help_text='File for evidence (eg. screenshot, log file, etc.)', null=True, upload_to='db/attachment/', verbose_name='File'),
        ),
    ]
