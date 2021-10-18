a, b = input().split()
b = list(b)
n = len(a)
max_cnt = 0
while len(a) <= len(b):
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    b = b[1:]
print(n - max_cnt)