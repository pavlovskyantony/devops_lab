words = map(str, input().split())
row1 = set('qwertyuiop')
row2 = set('asdfghjkl')
row3 = set('zxcvbnm')
results = []
for w in words:
    word = set(w.lower())
    if word == row1 or word == row2 or word == row3:
        results.append(w)
print(results)
print(word)
