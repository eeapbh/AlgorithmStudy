import sys

sys.stdin = open('input.txt', 'r')
arr = [list(map(int, input())) for _ in range(4)]

def spin(idx, d):
    if d == 1:
        tmp = arr[idx].pop()
        arr[idx].insert(0, tmp)
    if d == -1:
        tmp = arr[idx].pop(0)
        arr[idx].append(tmp)
def left(idx, d):
    if idx < 0:
        return
    if arr[idx][2] != arr[idx + 1][6]:
        left(idx-1, -d)
        spin(idx, d)

def right(idx, d):
    if idx > 3:
        return
    if arr[idx][6] != arr[idx - 1][2]:
        right(idx+1, -d)
        spin(idx, d)
k = int(input())
for i in range(k):
    idx, d = map(int, input().split())
    # print(arr)
    left(idx-2, -d)
    right(idx, -d)
    spin(idx - 1, d)
# print(arr)
ans = 0
for i in range(4):
    # print(arr[i][0])
    if i == 0:
        if arr[i][0] == 1:
            ans += 1
    if i == 1:
        if arr[i][0] == 1:
            ans += 2
    if i == 2:
        if arr[i][0] == 1:
            ans += 4

    if i == 3:
        if arr[i][0] == 1:
            ans += 8
print(ans)


