n = 4
queries = [[0, 1], [0, 2], [0, 3], [3, 4], [1, 5], [1, 6],
           [2, 7], [1, 9], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
ans = []
queue = [[] for _ in range(n)]
cnt = 0
star = 0
m = len(queries)
for q in queries:

    if cnt == 1:
        ans.append(queue[star].pop(0))
    if q[0] >=0:
        queue[q[0]].append(q[1])
    if q[0] == -1:
        while 1:
            if cnt+1 == m:
                break
            if queue[star] != []:
                break
            star = (star+1)%n
        ans.append(queue[star].pop(0))
        star = (star+1)%n
    cnt += 1
print(queue)
print(ans)