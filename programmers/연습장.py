import requests

url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
token = 'c4cd392f7a2cb2436dc15453246ae238'

nn= [-1,5,60]
tt = [-1,5,10]
di,dj = [0,0,1,-1], [1,-1,0,0]

def start(token,problem):
    uri = url + '/start'
    h = {'X-Auth-Token' : token, 'Content-Type': 'application/json' }
    d = {'problem' : problem}

    return requests.post(uri, params = d, headers = h).json()

dic = start(token, 1)
auth_key = dic['auth_key']

def location(key):

    uri = url + '/locations'
    h = {'Authorization':key, 'Content-Type':'application/json'}
    return requests.get(uri, headers = h).json()

def Trucks(key):
    uri = url + '/trucks'
    h = {'Authorization':key, 'Content-Type':'application/json'}
    return requests.get(uri, headers = h).json()

def Simulate(key):

    uri = url + '/simulate'
    h = {'Authorization':key, 'Content-Type':'application/json'}
    d = { "commands": [
         { "truck_id": 0, "command": [2, 5, 4, 1, 6],
           "truck_id": 1, "command": [2, 5, 4, 1, 6],
           "truck_id": 2, "command": [2, 6],
           "truck_id": 3, "command": [2, 1, 6],
           "truck_id": 4, "command": [2, 5, 4, 1, 6]}

       ]}

    return requests.put(uri, json=d ,headers = h).json()


def Score(key):
    uri = url + '/score'
    h = {'Authorization':key, 'Content-Type':'application/json'}
    return requests.get(uri, headers = h).json()
print(start(token, 1))
print('=========')
print(location(auth_key))
print('=========')
print(Trucks(auth_key))
print('=========')
for i in range(720):
    print(Simulate(auth_key))
    print(Trucks(auth_key))
    print(location(auth_key))
    print(i)
print(Simulate(auth_key))
print('=========')
print(Score(auth_key))

