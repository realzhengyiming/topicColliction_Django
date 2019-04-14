# Generated by Django 2.0.3 on 2018-06-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tropic', '0004_auto_20180421_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionContent', models.TextField()),
                ('missionDesc', models.TextField()),
                ('missionState', models.TextField()),
                ('AsyncTime', models.DateTimeField(auto_now=True)),
                ('username', models.TextField()),
                ('missionDealine', models.DateTimeField()),
            ],
        ),
    ]
