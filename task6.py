a, y = map(int, input().split())
scores = [map(float, input().split()) for n in range(y)]
[print(sum(student) / len(student)) for student in zip(*scores)]
