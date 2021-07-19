n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
tmp = []
for i in range(len(arr)):
    tmp.append(arr[i] + i)
tmp.sort(reverse=True)
print(tmp[0] + 2)
