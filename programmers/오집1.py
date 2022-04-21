tstring = "this is {template} {template} is {state}"
variables = [["template", "{state}"], ["state", "{template}"]]
def solution(tstring, variables):
    answer = ''

    cnt = 0
    while 1:
        n = len(tstring)
        cnt += 1
        if cnt > 2:
            break
        save = set()
        i = 0
        st = 0
        ed = 0
        while i < n:
            if tstring[i] == '{':
                st = i
            if tstring[i] == '}':
                ed = i
                tmp = tstring[st:ed + 1]
                r = tmp[1:-1]
                for v in variables:
                    if v[0] == r:
                        save.add((tmp, v[1]))
                        break
            i += 1

        for s in save:
            answer = tstring.replace(s[0], s[1])
            tstring = answer
    return answer

print(solution(tstring, variables))