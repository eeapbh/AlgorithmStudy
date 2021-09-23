# lines = list(input())
lines =   [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

def solution(lines):

    log = []

    for i in lines:
        a, b, c = i.split()
        time = c[:-1]
        time = float(time)
        end = int(b[0:2])*3600 + int(b[3:5])*60 + int(b[6:8]) + float("0"+b[8:12])
        start = end - time + 0.001
        # print(start)
        # print(start*1000)
        start = int(start*1000)

        # print(end)
        # print(end*1000)
        end = int(end * 1000)


        log.append([start, end])
    print(log)
    answer = 0
    for x in log:
        answer = max(answer, throughput(log, x[0], x[0] + 1000),
                     throughput(log, x[1], x[1] + 1000))



    return answer

def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt


print("답",solution(lines))