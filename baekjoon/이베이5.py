from itertools import permutations
P = ["21","123","111","11"]


def check(word):
    if word == word[::-1]:
        return 1
    else:
        return -1
    # m = len(word)
    # for i in range(m//2):
    #     if word[i] == word[m-1-i]:
    #         continue
    #     else:
    #         return -1
    # return 1


def solution(P):
    answer = []
    n = len(P)
    arr = [i for i in range(n)]
    pattern = list(permutations(arr, n))
    print(pattern)
    save = []
    for a in pattern:
        for j in range(0, n, 2):
            tmp = P[a[j]] + P[a[j+1]]
            # print(tmp)
            if check(tmp) == 1:
                continue
            else:
                break
        else:
            save.append(a)
    ans = set()
    for s in save:
        for i in range(n):
            if s[i] == 0:
                if i % 2 == 0:
                    ans.add(s[i+1])
                else:
                    ans.add(s[i-1])
    # print('답',save)

    for an in ans:
        answer.append(P[an])



    return answer

print(solution(P))