# Generated by Django 3.2.4 on 2021-07-09 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='show_description',
            new_name='short_description',
        ),
    ]
