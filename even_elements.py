input_array = [int(i) for i in input().split()]
i = 0
output = []
for item in input_array:
    if i % 2 == 0:
        output.append(item)
    i += 1
print(output)
