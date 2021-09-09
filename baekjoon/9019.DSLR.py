import sys
from collections import deque

def check(a, b):
    q = deque()
    q.append((a, ''))
    arr[a] = 1
    while q:
        a, ans = q.popleft()
        if a == b:
            return ans
        if 2*a <= 9999 and arr[a * 2] == 0:
            arr[a * 2] = 1
            q.append((2*a, ans + 'D'))
        if 2*a > 9999 and arr[(2*a) % 10000] == 0:
            arr[(2*a)%10000] = 1
            q.append(((2*a)%10000, ans + 'D'))
        if a - 1 >= 0 and arr[a - 1] == 0:
            arr[a - 1] = 1
            q.append([a - 1, ans + 'S'])
        if a - 1 < 0 and arr[9999] == 0:
            arr[9999] = 1
            q.append([9999, ans + 'S'])

        nx = int((a % 1000) * 10 + a / 1000)
        if arr[nx] == 0:
            arr[nx] = 1
            q.append((nx, ans + 'L'))
        nx = int((a % 10) * 1000 + a / 10)
        if arr[nx] == 0:
            arr[nx] = 1
            q.append((nx, ans + 'R'))
t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    arr = [0]*10000
    print(check(a, b))