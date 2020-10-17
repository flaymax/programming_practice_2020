import numpy as np


def tr(a, h):
    return a*(h**2)/2


def kr(r):
    return np.pi*r*r


def pr(a, b):
    return a*b


def vote_for(n):
    if n == 1:
        return tr(int(input('введите сторону:')),int(input('введите высоту:')))
    elif n == 2:
        return kr(int(input('введите радиус:')))
    elif n == 3:
        return pr(int(input('введите а:')),int(input('введите b:')))
    else:
        return vote_for(int(input('не получилось, введите еще раз:')))


print('Чтобы вычислить:\nплощадь трeугольника, введите 1 \nплощадь круга, введите 2\nплощадь прямоугольника, '
      'введите 3\n')
print(vote_for(int(input())))
