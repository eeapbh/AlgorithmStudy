n = 437674
k = 3


def solution(n, k):
    answer = 0

    m = change(n, k)
    arr = list(m.split('0'))
    li = []
    for a in arr:
        if a == '':
           continue
        else:
            li.append(int(a))
    print(li)
    N = max(li) + 1
    arr2 = [1]*N
    arr2[0] = -1
    arr2[1] = -1
    for i in range(2, N//2 + 1):
        if arr2[i] == 1:
            for j in range(2*i, N, i):
                arr2[j] = -1
    for a in li:
        if a == '':
            continue
        if checkPrime(a, arr2) == 1:
            answer += 1

    return answer


def change(n, k):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, k)
        tmp += str(mod)
    return tmp[::-1]

def checkPrime(x, arr2):

    if arr2[x] == 1:
        return 1
    else:
        return -1
print(solution(n, k))