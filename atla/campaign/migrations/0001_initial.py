# Generated by Django 3.2.6 on 2021-09-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('era', models.CharField(choices=[('Kyoshi’s Era', 'Kyoshi’s Era'), ('Roku’s Era', 'Roku’s Era'), ('The Hundred Year War', 'The Hundred Year War'), ('Aang’s Era', 'Aang’s Era'), ('Korra’s Era', 'Korra’s Era')], max_length=25)),
                ('scope', models.TextField(blank=True)),
                ('group_focus', models.CharField(blank=True, max_length=255)),
                ('group_focus_details', models.TextField(blank=True)),
                ('act_one', models.TextField(blank=True)),
                ('act_two', models.TextField(blank=True)),
                ('act_three', models.TextField(blank=True)),
                ('non_player_characters', models.TextField(blank=True)),
                ('other_notes', models.TextField(blank=True)),
            ],
        ),
    ]
