# Generated by Django 2.0.3 on 2018-06-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tropic', '0006_todotable_updateversion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todotable',
            old_name='updateVersion',
            new_name='idOnClient',
        ),
    ]
