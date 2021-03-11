arr = [0]*91
word = input()
for w in word:
    if ord(w) >= 97:
        arr[ord(w)-32] += 1
    else:
        arr[ord(w)] += 1

maxIndex = max(arr)
if arr.count(maxIndex) >= 2:
    print('?')
else:
    print(chr(arr.index(maxIndex)))
