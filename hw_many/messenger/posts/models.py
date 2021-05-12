from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    time = models.DateTimeField(verbose_name='Время отправки', auto_now_add=True)
    text = models.TextField(verbose_name='Текст сообщения')

    author = models.ForeignKey(
        to='users.User',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-time',)