t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().split())
    b = list(input().split())
    c = list(input().split())
    save = []
    for i in b:
        save.append((b.index(i), a.index(i)))
    # print(save)
    save.sort(key=lambda x:x[1])
    # print(save)
    for s in save:
        print(c[s[0]], end=' ')
    print()