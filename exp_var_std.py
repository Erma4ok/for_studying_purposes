def expectation(lst):
    exp = 0
    for elem in lst:
        mult = elem[0] * elem[1]
        exp += mult
    return exp

def variation(lst):
    var = 0
    exp = expectation(lst)
    for elem in lst:
        mult = ((elem[0] - exp) ** 2) * elem[1]
        var += mult
    return var

def std(lst):
    return variation(lst) ** 0.5


x = list(map(int, input('Введи последовательность целых чисел x через пробел: ').split()))
p = list(map(float, input('Введи последовательность вероятностей p (с точкой!!!) через пробел: ').split()))
x_p = list(zip(x, p))

print('Математическое ожидание:', expectation(x_p))
print('Дисперсия:', round(variation(x_p), 4))
print('Стандартное отклонение:', round(std(x_p), 5))