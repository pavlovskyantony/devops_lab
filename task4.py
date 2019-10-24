n = int(input())
arr = list(map(int, input().split()))

result1 = 0
for x in arr:
    if x > 0:
        result1 += x
result2 = 1
start = arr.index(min(arr))
end = arr.index(max(arr))
if end < start:
    for i in arr[end + 1: start]:
        result2 *= i
else:
    for i in arr[start + 1: end]:
        result2 *= i

print("{0} {1}".format(result1, result2))
