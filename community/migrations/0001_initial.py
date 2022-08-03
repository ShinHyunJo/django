# Generated by Django 3.2.13 on 2022-07-13 11:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('regdate', models.DateTimeField(default=datetime.datetime.now)),
                ('thumbup', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('contents', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'community_review',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cno', models.IntegerField()),
                ('comments', models.TextField()),
                ('regdate', models.DateTimeField(default=datetime.datetime.now)),
                ('rno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='community.review')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'community_comment',
                'ordering': ['cno'],
            },
        ),
    ]
