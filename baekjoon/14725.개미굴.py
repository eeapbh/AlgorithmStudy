n = int(input())
dic = {}
for _ in range(n):
    arr = list(input().split())
    for i in range(2, len(arr)):
        if dic.get(arr[1]) == None:
            dic[arr[1]] = []
            dic[arr[1]].append((i-1, arr[i]))
        else:
            dic[arr[1]].append((i-1, arr[i]))
# print(dic)
sdic = sorted(dic.items())
for s in sdic:
    s[1].sort(key=lambda x:x[1])
# print(sdic)

for s in sdic:
    print(s[0])
    for a in s[1]:
        print(a[0]*'--',end='')
        print(a[1])

##트라이 공부해야함