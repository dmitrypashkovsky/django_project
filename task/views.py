from django.shortcuts import render
from .models import Data, Result
from .forms import DataForm


# http://127.0.0.1:8000/task/add
# Представление, которое предназначено для отображения страницы ввода набора данных
def add(request):

    # Служебные переменные
    type_page = "home"
    headline = "Тестовое задание"
    title = "Добавление данных"
    path = "http://" + request.get_host() + "/task"

    # Получаем POST-запрос
    form = DataForm(request.POST or None)

    # Если был произведён POST-запрос
    if request.method == "POST" and form.is_valid():

        # Регистрируем переменные формы
        data = form.cleaned_data
        a = data["a"]
        b = data["b"]

        # Сохраняем данные или возвращаем ошибку
        if len(a) > 0 and len(b) > 0:
            result = form.save()
        elif len(a) == 0 and len(b) == 0:
            error = "Вы не ввели значения переменных!"
        elif len(a) == 0:
            error = "Вы не ввели значение переменной a!"
        elif len(b) == 0:
            error = "Вы не ввели значение переменной b!"

    return render(request, 'task/add.html', locals())


# http://127.0.0.1:8000/task/check
# Представление, которое предназначено для обработки введённых данных в БД
def check(request):

    # Служебные переменные
    type_page = "check"
    headline = "Тестовое задание"
    title = "Обработка всех наборов данных"
    path = "http://" + request.get_host() + "/task"

    # Получаем POST-запрос
    form = DataForm(request.POST or None)


    # Если был произведён POST-запрос
    if request.method == "POST" and form.is_valid():

        if Data.objects.all().count() > 0:
            Data.check_data(Data)
            success = "Была произведена обработка всех наборов данных. В результате чего были добавлены новые записи об исключениях и результатах в БД, а их список можно увидеть в двух воркерах."
        else:
            error = "Вы ещё не добавили ни одного набора данных!"
    else:
        error = "Чтобы запустить обработку набора данных, нужно нажать по кнопке в интерфейсе главной страницы!"

    return render(request, 'task/result.html', locals())


# http://127.0.0.1:8000/task/result
# Представление, которое предназначено для выполнения тестовой функции
def result(request):

    # Служебные переменные
    type_page = "result"
    headline = "Тестовое задание"
    title = "Выполнение тестируемой функции"
    path = "http://" + request.get_host() + "/task"

    # Получаем POST-запрос
    form = DataForm(request.POST or None)

    # Если был произведён POST-запрос
    if request.method == "POST" and form.is_valid():
        if Result.objects.all().count() > 0:
            Data.execute_function(Data)
            success = "Была выполнена тестовая функция. Результат этой функции можно увидеть в одном из воркеров."
        else:
            error = "Вы ещё не добавили ни одного набора данных!"
    else:
        error = "Чтобы запустить выполнение тестируемой функции, нужно нажать по кнопке в интерфейсе главной страницы! Перед выполнением этого действия, вначале нужно запустить обработку всех наборов данных."

    return render(request, 'task/result.html', locals())