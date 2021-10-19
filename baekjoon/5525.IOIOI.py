import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

ans = 0
pattern = 0
i = 0
while i < m-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        pattern += 1
        if pattern == n:
            ans += 1
            pattern -= 1
        i += 2
    else:
        pattern = 0
        i += 1
print(ans)