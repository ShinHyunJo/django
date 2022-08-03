# Generated by Django 3.2.13 on 2022-07-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'heart',
            },
        ),
    ]