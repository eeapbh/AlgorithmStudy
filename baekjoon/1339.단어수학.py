n = int(input())
arr = [input() for _ in range(n)]
visit = [0]* 10
rs = []
dic = {}
for a in arr:
    for i in range(len(a)):
        if a[i] in dic:
            dic[a[i]] += 10 **(len(a)-i-1)
        else:
            dic[a[i]] = 10 ** (len(a)-i-1)

# print(dic)
li = list(dic.values())
li.sort(reverse=True)
# print(li)
num = 9
ans = 0
for a in li:
    ans += a * num
    num -= 1
print(ans)