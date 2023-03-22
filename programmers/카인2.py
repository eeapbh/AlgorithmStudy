q1 = [3, 2, 7, 2]
q2 = [4, 6, 5, 1]


from collections import deque
def solution(q1, q2):
    tmp = q1 + q2
    q1 = deque(q1)
    q2 = deque(q2)
    answer = 0

    n = len(tmp)
    s = sum(q1) + sum(q2)
    if s % 2 == 1:
        return -1
    if max(tmp) > s //2:
        return -1

    while 1:
        if sum(q1) == sum(q2):
            break
        if sum(q1) > sum(q2):
            a = q1.popleft()
            q2.append(a)
            answer += 1
        else:
            a = q2.popleft()
            q1.append(a)
            answer += 1
    return answer

print(solution(q1, q2))