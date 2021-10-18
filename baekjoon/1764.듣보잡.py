n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
rs = sorted(list(set(a)&set(b)))
print(len(rs))
for i in rs:
    print(i)
