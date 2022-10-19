from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=200)
    text = models.TextField("Содержание")
    created_date = models.DateTimeField("Дата создания", default=timezone.now)
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
