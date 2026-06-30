from django.db import models

class Movies(models.Model):
    title = models.CharField('Назва фільму',max_length=50)
    author = models.CharField('Режисер',max_length=30)
    description = models.TextField('Опис фільму')
    year = models.IntegerField('Рік випуску')
    genre = models.CharField('Жанр',max_length=30)
    poster = models.ImageField(blank=True,null=True,upload_to='media/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
