s = input()

def solution(s):

    l = len(s)
    if l == 1:
        return 1
    save = []
    for i in range(1, l // 2 + 1):
        tmp = s[:i]
        ans = ''
        cnt = 1
        for j in range(i, l, i):
            if tmp == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    ans += tmp
                    tmp = s[j:j + i]
                    cnt = 1
                    continue
                else:
                    ans += str(cnt)
                    ans += tmp
                    tmp = s[j:j + i]
                    cnt = 1
        if cnt == 1:
            ans += tmp
            cnt = 1
        else:
            ans += str(cnt)
            ans += tmp
            cnt = 1
        save.append(len(ans))
    return min(save)

print(solution(s))





