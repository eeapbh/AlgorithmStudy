import sys
sys.stdin = open('input.txt', 'r')

import heapq
arr = []
n = int(input())
for i in range(n):
    d, v = map(int, input().split())
    arr.append([-v, d, v])
heapq.heapify(arr)
save = [0]*1001

while arr:
    tmp = heapq.heappop(arr)
    for i in range(tmp[1], 0, -1):
        if save[i] == 0:
            save[i] = tmp[2]
            break

print(save)
print(sum(save))


