import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
def check(line):
    m = len(line)
    for i in range(m):
        if line[i] == line[m - 1 - i]:
            continue
        else:
            return -1
    return 1
for _ in range(t):
    word = list(input())
    s = 0
    e = len(word) - 1
    cnt = 0
    while 1:
        if s >= e:
            break
        if word[s] == word[e]:
            s += 1
            e -= 1
            continue
        else:
            cnt += 1
            tmp1 = word[:s] + word[s+1:]
            tmp2 = word[:e] + word[e+1:]
            if check(tmp1) == 1 or check(tmp2) == 1:
                print(1)
                break
            else:
                print(2)
                break

    if cnt == 0:
        print(0)

