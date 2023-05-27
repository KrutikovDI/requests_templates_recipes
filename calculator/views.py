from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    for i, j in DATA['omlet'].items():
        DATA['omlet'][i] = j * servings

    context = {
        'omlet': DATA['omlet'],
        'servings': servings
    }
    return render(request, 'calculator/omlet.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    for i, j in DATA['pasta'].items():
        DATA['pasta'][i] = j * servings

    context = {
        'pasta': DATA['pasta'],
        'servings': servings
    }
    return render(request, 'calculator/pasta.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    for i, j in DATA['buter'].items():
        DATA['buter'][i] = j * servings

    context = {
        'buter': DATA['buter'],
        'servings': servings
    }
    return render(request, 'calculator/buter.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/omlet.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
