fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
import math
def solution(fees, records):
    answer = []
    dic = {}
    #기본시간, 기본요금, 단위시간, 단위요금

    for r in records:
        t, carNum, a = r.split()
        dic[carNum] = []

    for r in records:
        t, carNum, a = r.split()

        h, m = t.split(":")
        time = int(h)*60 + int(m)

        dic[carNum].append(time)
    # print(dic)
    for k, v in dic.items():
        if len(v) % 2 != 0:
            dic[k].append(23*60 + 59)

    dic2 = {}
    for k, v in dic.items():
        tmp = 0
        for i in range(0, len(v), 2):
            tmp += v[i+1] - v[i]


        if tmp > fees[0]:
            tmp -= fees[0]
            tmp = fees[1] + math.ceil(tmp/fees[2])*fees[3]
            dic2[int(k)] = tmp

        elif tmp <= fees[0]:
            dic2[int(k)] = fees[1]
    # print(dic2)
    sortdic = sorted(dic2.items())
    # print(sortdic)
    for s in sortdic:
        answer.append(s[1])


    return answer

print(solution(fees, records))