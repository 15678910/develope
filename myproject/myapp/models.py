from django.db import models

# Create your models here.
class NOtice(models.Model):
    title = models.CharField(max_length=200)
    likeCount = models. IntegerField()
    voewCpimt = models. IntegerField()
    contents = models.TextField()

    def __str__(self):
        return f'제목 : {self.title}, 좋아요 수 : {self.likeCount}', '조회수 : {self.viewCount}'
