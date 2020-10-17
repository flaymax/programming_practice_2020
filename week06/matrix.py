def summa(a, n):
    s = 0
    if n == 1:
        for i in range(len(a)):
            s += a[i][i]
        return s
    elif n == 2:
        for i in range(len(a)):
            s += a[i][-i-1]
        return s
    else:
        return(summa(a,int(input('вы не справились, введите еще раз:'))))


print('Введите порядок квадратной матрицы: ')
a = []
n = int(input())
for i in range(n):
    a.append(input().split(' '))
    for j in range(n):
        a[i][j] = int(a[i][j])
print('Чтобы вычислить сумму элементов главной диагонали введите 1, побочной 2: ')
print(summa(a, int(input())))
