n = int(input())
li = [0] * n
ans = 0

def daegak(x):
    for i in range(x):
        if li[x] == li[i] or abs(li[x]-li[i]) == x - i:
            return False
    return True

def check(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        li[x] = i
        if daegak(x):
            check(x+1)

check(0)
print(ans)