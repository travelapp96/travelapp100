# Generated by Django 4.1.7 on 2023-02-25 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_team_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='name_1',
        ),
    ]
