from collections import deque

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    q = deque()
    q.append((0, 0))


    while len(q)> 0:
        Cidx, value = q.popleft()
        if Cidx == n:
            if value == target:
                answer += 1
        else:
            q.append((Cidx + 1, value + numbers[Cidx]))
            q.append((Cidx +1, value - numbers[Cidx]))
    return answer
print(solution([1, 1, 1, 1, 1], 3))
