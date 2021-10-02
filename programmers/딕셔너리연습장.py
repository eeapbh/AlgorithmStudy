change_list = []
for i in range(1, 31):
    dic = {}
    dic['id'] = i
    dic['grade'] = 100 + i
    change_list.append(dic)
print('0일때',change_list)
print(change_list[0].keys())


sort_waiting_line = []
user_info = change_list
waiting = {'waiting_line': [{'id': 13, 'from': 1}, {'id': 17, 'from': 1}, {'id': 24, 'from': 1}, {'id': 4, 'from': 1}, {'id': 8, 'from': 1}, {'id': 9, 'from': 1}, {'id': 14, 'from': 1}, {'id': 2, 'from': 1}, {'id': 28, 'from': 1}, {'id': 6, 'from': 1}, {'id': 15, 'from': 1}, {'id': 18, 'from': 1}, {'id': 25, 'from': 1}, {'id': 11, 'from': 1}, {'id': 21, 'from': 1}, {'id': 23, 'from': 1}, {'id': 3, 'from': 1}, {'id': 26, 'from': 1}, {'id': 20, 'from': 1}, {'id': 1, 'from': 1}, {'id': 30, 'from': 1}, {'id': 7, 'from': 1}, {'id': 5, 'from': 1}, {'id': 10, 'from': 1}, {'id': 16, 'from': 1}, {'id': 12, 'from': 1}, {'id': 22, 'from': 1}, {'id': 29, 'from': 1}, {'id': 19, 'from': 1}, {'id': 27, 'from': 1}]}
# waiting['waiting_line']
for w in waiting['waiting_line']:
    tmp = []
    for user in user_info:
        if w['id'] == user['id']:
            tmp = [w['id'], w['from'], user['grade']]
            sort_waiting_line.append(tmp)
sort_waiting_line.sort(key=lambda x:(x[1], x[2]))
print(sort_waiting_line)