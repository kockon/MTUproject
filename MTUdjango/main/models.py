from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Вопрос')
    date = models.DateTimeField('Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answers(models.Model):
    answer = models.TextField('Ответ')
    date = models.DateTimeField('Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'