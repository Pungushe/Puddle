from django.contrib.auth.models import User
from django.db import models

from item.models import Item

class Conversation(models.Model):
    item=models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE, verbose_name='Товар')
    members=models.ManyToManyField(User, related_name='conversations', verbose_name='Участники')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at=models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    class Meta:
        ordering = ('-modified_at',)
        verbose_name = 'Взаимодействие с пользователем'
        verbose_name_plural = 'Взаимодействие с пользователями'
    
   

class СonversationMessage(models.Model):
    conversation=models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE, verbose_name='Обсуждение')
    content=models.TextField(verbose_name='Сообщение')
    created_at=models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    created_by=models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE, verbose_name='Cоздал')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.content    

