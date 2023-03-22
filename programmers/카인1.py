survey =["AN", "CF", "MJ", "RT", "NA"]
choices =[5, 3, 2, 7, 5]
def solution(survey, choices):
    answer = ''
    jipo = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    check = [[0, 0],[0, 0],[0, 0],[0, 0]]
    n = len(survey)
    rs = []
    for i in range(n):
        if choices[i]<4:
            rs.append((survey[i][0], 4-choices[i]))
        elif choices[i]>4:
            rs.append((survey[i][1], choices[i] - 4))
    print(rs)
    for r in rs:
        for i in range(4):
            if r[0] in jipo[i]:
                check[i][jipo[i].index(r[0])] += r[1]
    print(check)
    for i in range(4):
        if check[i][0] > check[i][1]:
            answer += jipo[i][0]
        elif check[i][0] == check[i][1]:
            answer += jipo[i][0]
        else:
            answer += jipo[i][1]
    return answer

print(solution(survey, choices))