# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20180130_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='location',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='type',
            new_name='level',
        ),
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
