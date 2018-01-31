# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_wall_app', '0003_auto_20180126_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='moderated',
            field=models.BooleanField(default=False),
        ),
    ]
