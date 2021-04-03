n = int(input())
cnt = 0
i = 665
while 1:
    i += 1
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
