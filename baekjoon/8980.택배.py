import sys
sys.stdin = open('input.txt', 'r')

n, c = map(int, input().split())
m = int(input())
visit = [c]*21
save = []
arr = [list(map(int, input().split())) for _ in range(m)]

arr.sort(key=lambda x:x[1])
print(arr)
# truck = 0
# ans = 0
# for a in arr:
#     if a[0] >= 2:
#         for s in save:
#             if s[0] == a[0]:
#                 truck -= s[1]
#                 visit[a[0]] -= s[1]
#                 ans += s[1]
#
#         tmpSave = []
#         for s in save:
#             if s[0] != a[0]:
#                 tmpSave.append(s)
#         save = tmpSave[::]
#
#
#     if truck + a[2] <= c:
#         visit[a[1]] += a[2]
#         truck += a[2]
#         save.append((a[1], a[2]))
#     else:
#         tmp = 0
#         tmp = c - truck
#         if tmp == 0:
#             continue
#         visit[a[1]] += tmp
#         truck += tmp
#         save.append((a[1], tmp))
# print(save)
# print(ans)
# for s in save:
#     ans += s[1]
# print(ans)