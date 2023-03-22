alp = 0
cop = 0
problems = 	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
def solution(alp, cop, problems):
    answer = 0
    a, b = 0, 0
    for p in problems:
        if p[0] > a:
            a = p[0]
        if p[1] > b:
            b = p[1]
    print(a, b)
    problems.sort(key=lambda x:(x[0], x[1]))
    print(problems)
    n = len(problems)
    check = [0]*n
    while 1:
        if alp >= a and cop >= b:
            break
        for i in range(n):
            if alp >= problems[i][0] and cop >= problems[i][1]:
                alp += problems[i][2]
                cop += problems[i][3]
                answer += problems[i][-1]
                check[i] += 1
            else:
                if sum(check) == 0:
                    answer += problems[i][0] - alp + problems[i][1] - cop
                    if alp < problems[i][0]:
                        alp = problems[i][0]
                    if cop < problems[i][1]:
                        cop = problems[i][1]
                else:
                    n1, n2 = 9999, 9999
                    if problems[i - 1][2] != 0:
                        n1 = (problems[i][0] - alp) // problems[i - 1][2]
                    if problems[i - 1][3] != 0:
                        n2 = (problems[i][1] - cop) // problems[i - 1][3]
                    alp += min(n1, n2) * problems[i - 1][2]
                    cop += min(n1, n2) * problems[i - 1][3]
                    answer += min(n1, n2)*problems[i-1][-1]
    return answer

print(solution(alp, cop, problems))