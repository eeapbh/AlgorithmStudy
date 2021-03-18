n = int(input())
i = 1
while 1:
    if n == 1:
        break
    i += 1
    if n % i == 0:
        print(i)
        n = n//i
        i = 1
