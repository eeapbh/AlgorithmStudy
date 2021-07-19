import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for _ in range(t):
    arr = [0, 1]
    idx = 0
    n = int(input())
    while 1:
        tmp = arr[idx] + arr[idx + 1]
        if tmp > n:
            arr.append(tmp)
            break
        arr.append(tmp)
        idx += 1
    trg = n
    save = []
    while 1:
        if trg == 0:
            break
        for i in range(len(arr)):
            if arr[i] > trg:
                save.append(arr[i-1])
                trg -= arr[i-1]
                break

    save.reverse()
    print(*save)
