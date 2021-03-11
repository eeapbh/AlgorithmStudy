line = list(input())
ans = 0
trg = 0
for l in line:
    if trg == 0:
        if l != ' ':
            ans += 1
            trg = 1
    else:
        if l == ' ':

            ans += 1
            trg = 0

if line[-1] == ' ':
    print(ans//2)
else:
    print(ans//2 + 1)


