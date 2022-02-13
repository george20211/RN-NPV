from django.shortcuts import render


def calc_npv(k, year, start_year=2020):
    '''Расчет NPV на каждый год'''
    n = year - start_year
    income = [1000, 1000, 500, 500, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000]

    if n == 0:
        return round((income[n]/(1+k)**(n+1)), 2)
    return round((income[n]/(1+k)**(n+1) + calc_npv(k, year-1)), 2)


def index(request, k=0.2, year=2050):
    '''Выводим результат в шаблон'''
    npv = calc_npv(k, year)
    context = {
        'npv': npv,
    }
    return render(request, 'homepage.html', context)
