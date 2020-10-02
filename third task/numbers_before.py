lst = [int(i) for i in input().split()]
unique = []
for i in range(len(lst)):
    if lst[i] in unique:
        print('YES')
    else:
        unique.append(lst[i])
        print('NO')
