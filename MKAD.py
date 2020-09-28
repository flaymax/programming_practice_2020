length = 109
v = int(input())
t = int(input())
if v > 0:
    s = v*t
    while s > length:
        s -= length
    print(s)
else:
    s = v*t
    while s < - length:
        s += length
    print(length + s)