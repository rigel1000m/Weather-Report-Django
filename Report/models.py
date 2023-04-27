from django.db import models

# Create your models here.

class LastReport(models.Model):
    city = models.CharField(max_length=100, verbose_name='Название города')

    class Meta:
        verbose_name = 'Прогноз погоды'
        verbose_name_plural = 'Прогнозы'


    def __str__(self):
        return self.city