lst = [int(i) for i in input().split()]
unique = []
for i in range(len(lst)):
    if lst[i] not in unique and lst.count(lst[i]) == 1:
        unique.append(lst[i])
print(unique)
