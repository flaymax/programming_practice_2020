input_array = [int(i) for i in input().split()]
lst = [input_array[i] for i in range(0, len(input_array)) if i % 2 == 0]
print(lst)
