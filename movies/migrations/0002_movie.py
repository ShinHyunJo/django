# Generated by Django 3.2.13 on 2022-07-08 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('youtube_path', models.CharField(blank=True, max_length=200)),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'movies_movie',
            },
        ),
    ]