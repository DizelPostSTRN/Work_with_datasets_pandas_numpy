# находим медиану
def find_median(x):
    if len(x) % 2 == 0:
        return (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
    else:
        return x[len(x) // 2]


print(find_median([2, 4, 5, 6, 8]))


# находим среднее значение
def find_average(x):
    return sum(x) / len(x)


print(find_average([1, 2, 3, 4, 5]))


# находим размах
def find_range(x):
    x_copy = sorted(x)
    return abs(x_copy[-1] - x_copy[0])


print(find_range([5, 2, 8, 1, 3]))

# находим дисперсию в генеральной совокупности
'''Переменная x_average - это среднее значение чисел в наборе x.
Далее, функция проходит в цикле по всем числам в наборе x и для каждого числа 
суммирует квадрат разности между числом и средним значением x_average. 
Итоговая сумма variance представляет собой сумму квадратов отклонений от среднего 
значения исходного набора.
На последнем шаге функция возвращает значение variance, поделенное на количество 
чисел в наборе x, что и является общей дисперсией.'''


def find_general_variance(x, x_average):
    variance = 0
    for i in x:
        variance += (i - x_average) ** 2
    return variance / len(x)


print(find_general_variance([3, 4, 5, 7, 8], 5))
