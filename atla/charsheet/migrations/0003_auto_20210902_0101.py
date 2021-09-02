# Generated by Django 3.2.6 on 2021-09-02 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0002_character_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='background',
            field=models.CharField(choices=[('Military', 'Military'), ('Monastic', 'Monastic'), ('Outlaw', 'Outlaw'), ('Privileged', 'Privileged'), ('Urban', 'Urban'), ('Wilderness', 'Wilderness')], default='Military', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='demeanor',
            field=models.CharField(choices=[('Impatient', 'Impatient'), ('Sensitive', 'Sensitive'), ('Affable', 'Affable'), ('Enthusiastic', 'Enthusiastic'), ('Talkative', 'Talkative'), ('Impetuous', 'Impetuous')], max_length=15),
        ),
    ]
