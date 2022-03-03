n = 2320
def solution(n):
    answer = 0
    tmp = str(n)
    tmp = set(tmp)
    for t in tmp:
        if t == '0':
            continue
        if n % int(t) == 0:
            answer += 1
    return answer

print(solution(n))