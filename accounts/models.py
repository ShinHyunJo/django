# from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class User(models.Model):
#     id=models.AutoField(primary_key=True)
#     userid=models.CharField(max_length=18, unique=True)
#     passwd=models.CharField(max_length=18)
#     email=models.TextField()
#     regdate=models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         db_table = 'accounts_user'


class User(AbstractUser):
    userid = models.CharField(max_length=18)

    class Meta:
        db_table = 'accounts_user'


class Heart(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'heart'
