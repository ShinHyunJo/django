# Generated by Django 3.2.13 on 2022-07-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(null=True),
        ),
    ]