a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [i for i in a if i in b]
print(sorted(c))
