from django.shortcuts import render


# http://127.0.0.1:8000/task/add
# Представление, которое предназначено для отображения страницы ввода набора данных
def add(request):

    # Служебные переменные
    type_page = "home"
    headline = "Тестовое задание"
    title = "Добавление данных"
    path = "http://" + request.get_host() + "/task"

    return render(request, 'task/add.html', locals())


# http://127.0.0.1:8000/task/check
# Представление, которое предназначено для обработки введённых данных в БД
def check(request):

    # Служебные переменные
    type_page = "check"
    headline = "Тестовое задание"
    title = "Обработка всех наборов данных"
    path = "http://" + request.get_host() + "/task"

    return render(request, 'task/result.html', locals())


# http://127.0.0.1:8000/task/result
# Представление, которое предназначено для выполнения тестовой функции
def result(request):

    # Служебные переменные
    type_page = "result"
    headline = "Тестовое задание"
    title = "Выполнение тестируемой функции"
    path = "http://" + request.get_host() + "/task"

    return render(request, 'task/result.html', locals())