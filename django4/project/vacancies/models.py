from django.db import models

class Vacancies(models.Model):
    title = models.CharField('Назва',max_length=100)
    description = models.TextField('Опис')
    salary = models.DecimalField('Зарплата',max_digits=10,decimal_places=2)
    company = models.CharField('Компанія',max_length=50)
    location = models.CharField('Розташування',max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'