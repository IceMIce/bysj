# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=16)),
                ('user_sign', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(to='hospital.User'),
        ),
    ]
