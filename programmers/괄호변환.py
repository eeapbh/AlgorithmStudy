p = '()))((()'

def solution(p):
    answer = ''
    s = p[0]
    tmp = p[0]
    cnt1 = 1
    cnt2 = 0
    u, v = '', ''
    l = len(p)
    for i in range(1, l):
        if s == p[i]:
            tmp += p[i]
        else:
            cnt2 += 1
            tmp += p[i]
        if cnt1 == cnt2:
            v = p[i+1:]
            u = tmp
            break
    print(u)
    print(v)
    if check(u) == 1:
        answer = u
        answer += solution(v)
    elif check(u) == -1:

        temp = '('
        temp += solution(v)
        temp += ')'
        tmpu = u
        tmpu = tmpu[1:-1]
        newu = ''
        for t in tmpu:
            if t == '(':
                newu += ')'
            else:
                newu += '('
        temp += newu
        answer = temp

    return answer

def check(line):
    stack = []
    if line[0] == ')':
        return -1
    for i in line:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return -1
    return 1



print('답', solution(p))
