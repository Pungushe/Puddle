from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, verbose_name='Категории')
    name = models.CharField(max_length=255, verbose_name='Название')
    description=models.TextField(null=True, blank=True, verbose_name='Описание')
    image=models.ImageField(upload_to='item_images', null=True, blank=True, verbose_name='Изображение')
    is_sold=models.BooleanField(default=False, verbose_name='Продано')
    created_by=models.ForeignKey(User, related_name='items', verbose_name='Создал', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price=models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name



