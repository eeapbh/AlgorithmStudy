n = input()
long = len(n)
n = int(n)

for i in range(1, n):
    tmp = 0
    word = str(i)
    for w in word:
        tmp += int(w)
    tmp += i
    if tmp == n:
        print(i)
        break
else:
    print(0)