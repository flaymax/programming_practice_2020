def distance(x1, x2, y1, y2):
    return ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** 0.5


x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
print(distance(x1, x2, y1, y2))
