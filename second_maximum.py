lst = []
lst.append(int(input()))
i = 0
while lst[i] != 0:
    lst.append(int(input()))
    i += 1
lst = sorted(lst, reverse=True)
print(lst[1])
