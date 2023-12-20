from django.db import models
NULLABLE = {'blank': True, 'null': True}


class ModelA(models.Model):
    a_one = models.CharField(max_length=250, verbose_name='Название')
    a_two = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    a_three = models.CharField(max_length=250, verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.a_one}'

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели1'


class ModelB(models.Model):
    a_one = models.CharField(max_length=250, verbose_name='Название')
    a_two = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    a_three = models.CharField(max_length=250, verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.a_two}'

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели2'


class ModelC(models.Model):
    a_one = models.CharField(max_length=250, verbose_name='Название')
    a_two = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    a_three = models.CharField(max_length=250, verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.a_three}'

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели3'
