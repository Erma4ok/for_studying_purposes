from math import factorial

def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def bernulli(p, q, n, k):
    result = 0
    for num in k:
        result += C(n, num) * (p ** num) * (q ** (n - num))
    return result

p = float(input('Введи вероятность p (с точкой!!!): '))
q = float(input('Введи вероятность q (с точкой!!!): '))
n = int(input('Введи целое число n всех возможных событий: '))
k = list(map(int, input('Введи последовательность целых k, удволетворяющих условию, через пробел: ').split()))
print('Вероятность: ', round(bernulli(p, q, n, k), 5))
