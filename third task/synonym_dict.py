n = int(input())
dic = {}
for i in range(n):
    j , k = input().split()
    dic[j] = k
    dic[k] = j
print(dic[input()])
