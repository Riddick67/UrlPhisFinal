# Generated by Django 4.2.7 on 2024-02-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0011_modelselected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picklefile',
            name='file',
        ),
        migrations.AddField(
            model_name='picklefile',
            name='text_field',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
