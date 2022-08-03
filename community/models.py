from datetime import datetime
from django.db import models

# Create your models here.
from accounts.models import User
from movies.models import Movie


class Review(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    regdate=models.DateTimeField(default=datetime.now)
    thumbup=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    contents=models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'community_review'
        ordering = ['-id']

class Comment(models.Model):
    id=models.AutoField(primary_key=True)   # 댓글고유번호
    cno=models.IntegerField()               # 답글고유번호
    rno=models.ForeignKey(Review, on_delete=models.DO_NOTHING) # 본문글번호
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING) # 작성자번호
    comments=models.TextField()
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'community_comment'
        ordering = ['cno']

