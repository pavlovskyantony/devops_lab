words = map(str, input().split())
row1 = set('qwertyuiop')
row2 = set('asdfghjkl')
row3 = set('zxcvbnm')
results = []
for w in words:
    word = set(w.lower())
    if (word - row1) == set() or ((word - row2) == set()) or ((word - row3) == set()):
        results.append(w)
print(results)
print(word)
