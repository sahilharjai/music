# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('rating_of_track', models.CharField(default='3', choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Average'), ('4', 'Good'), ('5', 'Very Good')], max_length=1)),
                ('genres', models.ForeignKey(to='genres.Genre')),
            ],
        ),
    ]
