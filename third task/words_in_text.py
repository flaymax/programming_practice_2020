n = int(input())
words = set()
for i in range(n):
    words.update( input().split() )
print(len(words))


