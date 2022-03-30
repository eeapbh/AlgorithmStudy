logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]

def solution(logs):
    logs = ','.join(logs)
    logs = logs.split(',')
    newLogs = []
    ans = 0
    trg = 0
    for log in logs:

        if len(log) > 100:
            ans += 1
        else:
            newLogs.append(log)
    check = ['team_name', 'application_name', 'error_level', 'message']
    for l in newLogs:
        a = l.split(' :')
        a = ''.join(a)
        a = a.split(' ')

        if len(a) != 8:
            ans += 1
            continue
        elif a[0] != check[0] or a[2] != check[1] or a[4] != check[2] or a[6] != check[3]:
            ans += 1
            continue
        for i in range(1, 8, 2):
            for b in a[i]:
                if b == ' ':
                    ans += 1
                    trg = 1
                    break
                if 65<=ord(b)<=90 or 97<=ord(b)<=122:
                    continue
                else:
                    ans += 1
                    trg = 1
                    break
            if trg == 1:
                trg = 0
                continue
    return ans


print(solution(logs))