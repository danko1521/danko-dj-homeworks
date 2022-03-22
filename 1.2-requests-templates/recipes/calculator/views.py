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


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

def omlet(request):
    repice = DATA.get('omlet')
    context = {
        'repice' : repice
    }
    return render(request, 'calculator/probe.html', context)

# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def pasta(request):
    repice = DATA.get('pasta')
    context = {
        'repice' : repice
    }
    return render(request, 'calculator/probe.html', context)

def buter(request):
    repice = DATA.get('buter')
    context = {
        'repice' : repice
    }
    return render(request, 'calculator/probe.html', context)