m, n = map(int, input().split())
# for i in range(m, n+1):
#     if i == 1:
#         continue
#     else:
#         cnt = 0
#         for j in range(2, int(i ** (1/2)) + 1):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
n += 1
arr = [1]*n
for i in range(2, int(n ** 0.5)+1):
    if arr[i]:
        for j in range(2*i, n, i):
            arr[j] = 0
for k in range(m, n):
    if arr[k] and k>1:
        print(k)