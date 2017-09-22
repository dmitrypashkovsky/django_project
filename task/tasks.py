from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.test import TestCase


# data - набор данных
# exception - вызванная ошибка
# Возвращает набор данных и исключение
@shared_task
def return_exception(data, exception):
    return "Вызвано исключение для набора данных, где \n" + data + "\n" + exception

# data - набор данных
# status - 0 или 1 / False или True
# Возвращает набор данных и статус результата
@shared_task
def return_status(data, status):
    return data, status

# Возвращает результат тестовой функции
@shared_task
def test_func(value):
    import json
    d = json.loads(value)
    return {'result': d['a'] + d['b']}