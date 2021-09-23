record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    dic = {}
    ans = []
    for r in record:

        if r[0] == 'E' or r[0] == 'C':

            first, second, third = r.split()

            if first == 'Enter':
                dic[second] = third
            if first == 'Change':
                dic[second] = third


    for r in record:
        tmp = ''
        if r[0] == 'E':
            first, second, third = r.split()
            tmp = dic[second]
            tmp += '님이 들어왔습니다.'
            ans.append(tmp)
        elif r[0] == 'L':
            first, second = r.split()
            tmp = dic[second]
            tmp += '님이 나갔습니다.'
            ans.append(tmp)



    return ans

print(solution(record))