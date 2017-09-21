from django.db import models

# Модель, в которой хранится набор данных
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    a = models.CharField(max_length=16, blank=True, default=None)
    b = models.CharField(max_length=16, blank=True, default=None)

    class Meta:
        verbose_name = "Набор данных"
        verbose_name_plural = "Наборы данных"


# Модель, в которой хранятся исключения обработки данных
class Exception(models.Model):
    data = models.ForeignKey(Data)
    text = models.CharField(max_length=68, blank=True, default=None)


# Модель, в которой хранятся результаты обработки данных
class Result(models.Model):
    data = models.ForeignKey(Data)
    answer = models.CharField(max_length=13, blank=True, default=None)