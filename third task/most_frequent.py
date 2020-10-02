n = int(input())
count = {}
for i in range(n):
    line = input().split()
    for j in line:
        count[j] = 1 + count.get(j, 0)
count_max = max(count.values())
answer = min([key for key, val in count.items() if count_max == val])
print(answer)