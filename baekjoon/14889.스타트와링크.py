# from itertools import combinations, permutations
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# members = [m for m in range(n)]
#
# com = list(combinations(members, n//2))
# MIN = 987654321
# def check(arr1, arr2):
#     global MIN
#     p1 = list(permutations(arr1, 2))
#     p2 = list(permutations(arr2, 2))
#     sum1 = 0
#     sum2 = 0
#     for i in p1:
#         sum1 += arr[i[0]][i[1]]
#     for i in p2:
#         sum2 += arr[i[0]][i[1]]
#     if abs(sum1-sum2) < MIN:
#         MIN = abs(sum1-sum2)
#
#
# for c in com:
#     arr1 = c
#     arr2 = []
#     for i in members:
#         if i not in arr1:
#             arr2.append(i)
#     check(arr1, arr2)
# print(MIN)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [0 for _ in range(n)]
ans = 987654321
start, link = 0, 0
def check(idx, cnt):
    global ans
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start += arr[i][j]
                elif not visit[i] and not visit[j]:
                    link += arr[i][j]
        ans = min(abs(start-link), ans)
    for i in range(idx, n):
        if visit[i]:
            continue
        visit[i] = 1
        check(i+1, cnt+1)
        visit[i] = 0
check(0, 0)
print(ans)





