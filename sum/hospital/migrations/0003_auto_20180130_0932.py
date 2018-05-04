# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20180107_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
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
        migrations.RemoveField(
            model_name='oppointment',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Oppointment',
        ),
    ]
