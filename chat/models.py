from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Room(models.Model):
    name = models.CharField(
        max_length=128, verbose_name='Название'
    )
    invited = models.ManyToManyField(
        User, related_name='rooms', verbose_name='Участники'
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='chats', 
        verbose_name='Комната'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chats',
        verbose_name='Пользователь'
    )
    text = models.CharField(
        max_length=128, verbose_name='Сообщение'
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    
    def __str__(self):
        return f'{self.user}'
    
    
    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
