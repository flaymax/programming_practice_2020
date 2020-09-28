n = int(input())
if n//60 <= 23:
    x = (n//60)
    print(x, n % 60)
else:
    x = n//60
    while x > 23:
        x -= 24
    print(x, n % 60)
