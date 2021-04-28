from collections import deque
t = int(input())
for _ in range(t):
    n, idx = map(int, input().split())
    info = list(map(int, input().split()))
    arr = deque()
    for i in range(len(info)):
        arr.append((i, info[i]))
    cnt = 0
    while arr:
        if arr[0][1] == max(info):
            info.remove(arr[0][1])
            ans = arr.popleft()
            cnt += 1
            if ans[0] == idx:
                print(cnt)
                break
        else:
            tmp = arr.popleft()
            arr.append(tmp)



