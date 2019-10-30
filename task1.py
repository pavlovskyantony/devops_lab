n = int(input())
arr = map(int, input().split())
result = sorted(list(set(arr)))
print(result[-2])
