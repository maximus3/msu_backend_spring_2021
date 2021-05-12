from django.db import models


class Message(models.Model):
    time = models.DateTimeField(verbose_name='Время отправки', auto_now_add=True)
    text = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Chat(models.Model):
    messages = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'