from django.shortcuts import render


# http://127.0.0.1:8000/task/add
# Представление, которое предназначено для отображения страницы ввода набора данных
def add(request):
    return render(request, 'task/add.html', locals())


# http://127.0.0.1:8000/task/check
# Представление, которое предназначено для обработки введённых данных в БД
def check(request):
    return render(request, 'task/check.html', locals())


# http://127.0.0.1:8000/task/result
# Представление, которое предназначено для выполнения тестовой функции
def result(request):
    return render(request, 'task/result.html', locals())