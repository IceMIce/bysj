# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oppointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=500)),
                ('doctor', models.CharField(max_length=50)),
                ('time', models.DateTimeField(max_length=500)),
                ('user_id', models.ForeignKey(to='hospital.User')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='doctor',
            field=models.CharField(default=datetime.datetime(2018, 1, 7, 3, 21, 47, 383364, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
