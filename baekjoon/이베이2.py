from itertools import product
k = 1
stones = [4, 2, 2, 1, 4]
def solution(stones, k):
    answer = ''
    n = max(stones)
    m = len(stones)
    arr = [i for i in range(m)]
    pattern = []
    for i in product(arr, repeat=n):
        pattern.append(i)
    # print(arr)
    # print(pattern)

    save = []
    tmpStones = []
    for p in pattern:
        tmpStones = stones[::]
        trg = 0
        for i in p:
            if trg == -1:
                break
            for j in range(m):
                if i != j:
                    if tmpStones[j] > 0:
                        tmpStones[j] -=1

                    else:
                        trg = -1
                        break
                else:
                    tmpStones[j] += 1
        if tmpStones.count(0) == m-1 and sum(tmpStones) == k and trg == 0:
            save.append(p)
    # print('여기서 답잇음',save)
    if len(save) > 0:

        save.sort()
        ans = list(save[-1])
        for a in ans:
            answer += str(a)
    else:
        answer = '-1'


    return answer
print(solution(stones, k))