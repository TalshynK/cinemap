import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Name of article', max_length = 200)
    article_text = models.TextField('Text of Article')
    pub_date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Name of article', max_length = 50)
    comment_text = models.CharField('Name of article', max_length = 200)

    def __str__(self):
        return self.author_name

class Block(models.Model):
    img = models.ImageField(upload_to="movie_image",blank=True)
    block_explain =models.TextField('Explain of Movie')
    rating = models.FloatField(default=0.0)
    numberOfClicks = models.IntegerField(default=0)
    article_date = models.DateTimeField('date published')
