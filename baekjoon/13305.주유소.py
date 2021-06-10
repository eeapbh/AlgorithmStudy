import sys
sys.stdin = open('input.txt', 'r')


n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = cost[0] * dist[0]
c = cost[0]
for i in range(1, n-1):
    if cost[i] >= c:
        ans += c * dist[i]
    else:
        c = cost[i]
        ans += c * dist[i]
print(ans)
