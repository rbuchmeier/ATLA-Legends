# Generated by Django 3.2.6 on 2021-09-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0003_auto_20210902_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
