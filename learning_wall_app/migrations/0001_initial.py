# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(max_length=200, serialize=False, primary_key=True)),
                ('body', models.CharField(max_length=250, verbose_name=b'body of the post')),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(max_length=255)),
                ('moderator', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='learning_wall_app.User'),
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(to='learning_wall_app.User'),
        ),
    ]
