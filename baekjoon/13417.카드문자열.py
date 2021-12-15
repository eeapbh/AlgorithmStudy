t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    a = arr.pop(0)
    tmp = a
    while 1:
        if len(arr) == 0:
            break
        a = arr.pop(0)
        if ord(tmp[0]) >= ord(a):
            tmp = a + tmp
        else:
            tmp = tmp + a
    print(tmp)