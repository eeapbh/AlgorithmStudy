arr = [' ', ' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
ans = 0
for w in word:
    for i in range(10):
        if w in arr[i]:
            ans += i
print(ans + len(word))
