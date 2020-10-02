text = input()
text = text.upper()
text = text.split(' ')
dic = dict()
for i in text:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
answer = ''
for key, val in dic.items():
    answer += f'{key} {val} \n'
print(answer)
