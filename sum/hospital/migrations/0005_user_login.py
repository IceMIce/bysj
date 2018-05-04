# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20180423_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField(max_length=500)),
            ],
        ),
    ]
