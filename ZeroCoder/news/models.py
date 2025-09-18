from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




