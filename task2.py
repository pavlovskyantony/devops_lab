a, b, c, d = [int(i) for i in input().split()]

result = []
for x in range(-100, 100, 1):
    if (a * (x ** 3) + b * (x ** 2) + (c * x) + d) == 0:
        result.append(x)
print(result)
