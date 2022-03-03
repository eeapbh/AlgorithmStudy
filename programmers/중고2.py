
s = [3, -1, 0, 4]
# s = [1, 2, 3]
def solution(s):
    answer = 0
    n = len(s)
    trg = 1
    idx = 1
    while 1:
        if idx >= n:
            break
        if trg == 1:
            if s[idx] > s[idx - 1]:
                trg = -1
                idx += 1
                continue
            else:
                idx += 1
                answer += 1

        else:
            if s[idx] < s[idx - 1]:
                trg = 1
                idx += 1
                continue
            else:
                idx += 1
                answer += 1


    return answer

print(solution(s))