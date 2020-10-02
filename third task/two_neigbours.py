lst = [int(i) for i in input().split()]    # input_array
lst1 = [lst[i] for i in range(1, len(lst)-1) if lst[i] > lst[i-1] and lst[i] > lst[i+1]]
print(len(lst1))       # how many numbers?
