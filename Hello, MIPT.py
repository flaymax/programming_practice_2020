text = input()
n = int(input())
text1 = ''
for i in range(n-1):
    text1 += text+", "
text1 += text
print('Hello', text1, sep=', ')
