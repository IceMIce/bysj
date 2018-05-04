# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_login',
            name='user_sign',
            field=models.BooleanField(default=False),
        ),
    ]
