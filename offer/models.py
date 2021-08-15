from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Вид услуги')
    text = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(blank=True, verbose_name='Памятка')

    def __str__(self):
        return self.name