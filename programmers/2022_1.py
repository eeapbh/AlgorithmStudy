id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
def solution(id_list, report, k):
    answer = []
    dic = {}
    reportcheck = {}
    for i in id_list:
        dic[i] = set()
        reportcheck[i] = 0

    for r in report:
        a, b = r.split()
        dic[a].add(b)

    for key, v in dic.items():
        for a in v:
            reportcheck[a] += 1

    ban = []
    for key, v in reportcheck.items():
        if v >= k:
            ban.append(key)


    for d, v in dic.items():
        cnt =0
        for i in v:
            if i in ban:
                cnt += 1
        answer.append(cnt)



    return answer

print(solution(id_list, report, k))