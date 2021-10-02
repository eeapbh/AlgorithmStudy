import requests
url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
auth_token =  '2f855450e7275458af9faf9678ed9a48'
def start(token):
    uri = url + '/start'
    h = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    d = {'problem': 2}
    return requests.post(uri, params = d, headers = h).json()
def WaitingLine(key):
    uri = url + '/waiting_line'
    h = {'Authorization': key, 'Content-Type': 'application/json'}

    return requests.get(uri, headers = h).json()
def GameResult(key):
    uri = url + '/game_result'
    h = {'Authorization': key, 'Content-Type': 'application/json'}

    return requests.get(uri, headers = h).json()
def UserInfo(key):
    uri = url + '/user_info'
    h = {'Authorization': key, 'Content-Type': 'application/json'}

    return requests.get(uri, headers = h).json()

def Match(key, li):
    uri = url + '/match'
    h = {'Authorization': key, 'Content-Type': 'application/json'}
    d = {'pairs':li}
    return requests.put(uri, json = d, headers = h).json()

def ChangeGrade(key, li):
    uri = url + '/change_grade'
    h = {'Authorization': key, 'Content-Type': 'application/json'}
    d = {"commands": li}
    return requests.put(uri, json = d, headers = h).json()

def Score(key):
    uri = url + '/score'
    h = {'Authorization': key, 'Content-Type': 'application/json'}
    return requests.get(uri, headers = h).json()


dic = start(auth_token)
auth_key = dic['auth_key']

for i in range(596):
    print(i)
    waiting_line = WaitingLine(auth_key)
    user_info = UserInfo(auth_key)
    match_list = []
    sort_waiting_line = []
    for w in waiting_line['waiting_line']:
        tmp = []
        for user in user_info['user_info']:
            if w['id'] == user['id']:
                tmp = [w['id'], w['from'], user['grade']]
                sort_waiting_line.append(tmp)
    sort_waiting_line.sort(key=lambda x:(x[1], x[2]))
    # print('새로만든 waiting라인', sort_waiting_line)


    for j in range(0, len(sort_waiting_line), 2):
        if j == len(sort_waiting_line)-1:
            break
        else:
            tmp = [sort_waiting_line[j][0], sort_waiting_line[j+1][0]]
        match_list.append(tmp)

    game_result = GameResult(auth_key)
    # print(game_result)

    if i == 0:

        change_list = []
        for i in range(1, 901):
            dic = {}
            dic['id'] = i
            dic['grade'] = 9999
            change_list.append(dic)
        print('0일때',change_list)

    else:
        change_list = []
        for g in game_result['game_result']:
            tmp1 = {}
            tmp2 = {}
            grade1 = grade2 = 0
            for u in user_info['user_info']:
                if u['id'] == g['win']:
                    grade1 = u['grade']
                if u['id'] == g['lose']:
                    grade2 = u['grade']
            d = int(abs(grade1-grade2)*0.5) + 9999
            tmp1['id'] = g['win']
            tmp1['grade'] = grade1 + d
            tmp2['id'] = g['lose']
            if grade2 - d < 0:
                tmp2['grade'] = 0
            else:
                tmp2['grade'] = grade2 - d
            change_list.append(tmp1)
            change_list.append(tmp2)

            # print('등급바뀔애들 리스트좀보자', change_list)
    match = Match(auth_key, match_list)
    change_grade = ChangeGrade(auth_key, change_list)

    # print(waiting_line)

    # print(user_info)
    # print(game_result)
    # print(Match(auth_key))

    # print(change_grade)
print(Score(auth_key))
