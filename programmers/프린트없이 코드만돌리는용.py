import requests
url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
auth_token =  '2f855450e7275458af9faf9678ed9a48'
def start(token):
    uri = url + '/start'
    h = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    d = {'problem': 1}
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

for i in range(5):
    print(i)
    waiting_line = WaitingLine(auth_key)
    user_info = UserInfo(auth_key)
    match_list = []
    for j in range(0, len(waiting_line['waiting_line']), 2):
        # print('더블류', waiting_line['waiting_line'][j]['id'])
        if j == len(waiting_line['waiting_line'])-1:
            break
        else:
            tmp = [waiting_line['waiting_line'][j]['id'], waiting_line['waiting_line'][j + 1]['id']]
        match_list.append(tmp)
    # print('매치할애들 잘나오나 보자', match_list)
    game_result = GameResult(auth_key)
    # print(game_result)
    change_list = []
    if i == 0:
        pass
        # change_list = []
        # for i in range(1, 31):
        #     dic = {}
        #     dic['id'] = i
        #     dic['grade'] = 9999
        #     change_list.append(dic)
        # # print('0일때',change_list)

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
            d = abs(grade1-grade2) + 500
            tmp1['id'] = g['win']
            tmp1['grade'] = grade1 + d
            tmp2['id'] = g['lose']

            if grade2 - d < 0 :
                tmp2['grade'] = 0
            else:
                tmp2['grade'] = grade2 - d



            change_list.append(tmp1)
            change_list.append(tmp2)

            # print('등급바뀔애들 리스트좀보자', change_list)
    match = Match(auth_key, match_list)
    change_grade = ChangeGrade(auth_key, change_list)

    print(waiting_line)
    #
    print(user_info)
    # print(game_result)
    # print(Match(auth_key))

    # print(change_grade)
print(Score(auth_key))
