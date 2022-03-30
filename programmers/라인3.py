num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]


def solution(num_teams, remote_tasks, office_tasks, employees):
    ans = []
    save = []
    tmp = []

    team = [[] for _ in range(num_teams + 1)]


    for i in range(len(employees)):
        team[int(employees[i][0])].append((i + 1,employees[i][2:].split(' ')))


    check = [0]*(num_teams + 1)
    for i in range(1, num_teams+1):
        for t in team[i]:

            for a in t[1]:
                if a in office_tasks:
                    save.append(t[0])
                    check[i] += 1

    for i in range(1,len(employees)+ 1):
        if i not in save:
            ans.append(i)

    for i in range(1, num_teams + 1):
        if check[i] == 0:
            first =  team[i][0][0]
    ans.remove(first)
    return ans

print(solution(num_teams, remote_tasks, office_tasks, employees))