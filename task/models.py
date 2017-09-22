from django.db import models
from .tasks import return_exception, return_status, test_func
import json

# Модель, в которой хранится набор данных
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    a = models.CharField(max_length=16, blank=True, default=None)
    b = models.CharField(max_length=16, blank=True, default=None)

    # Метод, который проверяет все наборы данных и записывает все исключения и результаты
    def check_data(self):

        # Очищаем таблицы исключений и результатов
        Result.objects.all().delete()
        Exception.objects.all().delete()

        # Получаем все запипси модели Data
        data_all = Data.objects.all()

        for data in data_all:

            # Получаем типы введённых переменных
            type_a = self.check_value(data.a)
            type_b = self.check_value(data.b)

            # Проверяем их на соответствие типу int
            if self.check_exception(type_a, type_b) == True:

                # Название исключения
                name_except = self.name_exception(type_a, type_b)

                # Сохраняем исключение
                exception = Exception(data_id=data.id, text=name_except)
                exception.save()

                # Задача celery, которая показывает все исключения
                return_exception.apply_async(args=[self.json_transform(data.a, data.b), name_except],
                                             queue='return_exception',
                                             routing_key='return_exception.import')

                # Подготавливаем результат
                result = True
            else:
                result = False

            # Статус текущего результата
            status = self.json_return(result)

            # Сохраняем результат
            result = Result(data_id=data.id, status=status)
            result.save()

            # Задача celery, которая показывает все наборы данных и их статус
            return_status.apply_async(args=[self.json_transform(data.a, data.b), status],
                                         queue='return_status',
                                         routing_key='return_status.import')

    # Метод, который выполняет тестовую функцию
    def execute_function(self):

        # Получаем все записи модели Result
        result_all = Result.objects.all()

        for result in result_all:

            # Получаем текущий статус набора данных
            status = self.json_status(result.status)

            # Набор данных, подходящий для выполнения тестовой функции
            if status == 0:

                # Получаем выбранную запись по внешнему ключу
                data = Data.objects.get(id=result.data_id)

                # Формируем JSON-запрос
                values = self.json_transform(int(data.a), int(data.b))

                # Задача celery, которая выполняет тестовую функцию и возвращает результат
                test_func.apply_async(args=[values],
                                      queue='test_func',
                                      routing_key='test_func.import')

    def check_value(n):
        """ Проверить и вернуть тип переменной, которую ввёл пользователь

        :param n: переменная a или b
        :return: тип переменной
        """

        try:
            int(n)
            return "int"
        except ValueError:
            try:
                float(n)
                return "float"
            except ValueError:
                try:
                    complex(n)
                    return "complex"
                except ValueError:
                    try:
                        str(n)
                        if n == "True" or n == "False":
                            return "bool"
                        else:
                            return "str"
                    except ValueError:
                        return "none"

    def check_exception(a, b):
        """ Вернуть статус проверки переменных a и b

        :param a: переменная a
        :param b: переменная b
        :return: False/True
        """

        if a == "int" and b == "int":
            return False
        else:
            return True

    def name_exception(a, b):
        """ Формируем название текущего исключения

        :param a: переменная a
        :param b: переменная b
        :return: название вызванного исключения
        """

        if a != "int" and b != "int":
            name = "Переменные a и b не соответствуют типу int! " + "a - " + a + ", b - " + b
        elif a != "int":
            name = "Переменная a не соответствует типу int! " + " a - " + a
        elif b != "int":
            name = "Переменная b не соответствует типу int! " + " b - " + b

        return name

    # True - обнаружены исключения
    # False - переменные типа int
    # Возвращаем результат обработки
    def json_return(res):
        res = int(res)
        return json.dumps({'result': res}, sort_keys=False, indent=1)

    # Формируем JSON-запрос
    def json_transform(a, b):
        return json.dumps({'a': a, 'b': b}, sort_keys=True, indent=1)

    # Возвращаем статус результата обработки
    def json_status(value):
        import json
        d = json.loads(value)
        return d['result']

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
    status = models.CharField(max_length=17, blank=True, default=None)