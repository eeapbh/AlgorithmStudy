n = 6
k = 3
bulbs = "RBGRGB"
def check(b):
    m = len(b)
    tmpb = b[::]
    for i in range(m-k+1):
        for j in range(i, i+3):
            if tmpb[j] == 'R':
                tmpb[j] = 'G'
            elif tmpb[j] == 'G':
                tmpb[j] = 'B'
            else:
                tmpb[j] = 'R'


def solution(n, k, bulbs):
    bulbs = list(bulbs)
    answer = -2
    m = len(bulbs)
    save = []
    save.append(bulbs)
    print(save)
    cnt = 0
    while 1:
        cnt += 1
        s = save.pop()

        if s.count('R') == m:
            answer = cnt
            break
        for i in range(m-k+1):
            tmpBulbs = s[::]
            for j in range(i, i + k):
                if tmpBulbs[j] == 'R':
                    tmpBulbs[j] = 'G'
                    continue
                elif tmpBulbs[j] == 'G':
                    tmpBulbs[j] = 'B'
                    continue
                elif tmpBulbs[j] == 'B':
                    tmpBulbs[j] = 'R'
                    continue
            save.append(tmpBulbs)
        print(cnt, save)
        if cnt == 5:
            break
    return answer
solution(n, k, bulbs)