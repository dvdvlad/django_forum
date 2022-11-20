from django.db import models


class Articles(models.Model):
    articles = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    user_creater = models.CharField('Никнейм пользователя', max_length=50)

    def __str__(self):
        return self.articles
