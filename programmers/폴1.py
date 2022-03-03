from itertools import combinations
def solution(arr, k, t) :
    answer = 0
    li = []
    for i in range(k, len(arr)+1):
        li.extend(list(combinations(arr, i)))

    for l in li:
        if sum(l) <=t:
            answer += 1


    return answer



arr = [1, 2, 3, 2]
k = 2
t = 2

print(solution(arr, k, t))