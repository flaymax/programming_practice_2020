lst = [int(i) for i in input().split()]
lst1 = lst.copy()
a, b = min(lst1), max(lst1)
lst[lst.index(min(lst))], lst[lst1.index(max(lst1))] = b, a
print(lst)