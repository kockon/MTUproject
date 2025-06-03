from django.db import models


class Users(models.Model):
    nickname = models.CharField('Ник', max_length=50)
    password = models.CharField('Пароль', max_length=100)
    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birth = models.CharField('Дата рождения', max_length=250)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
