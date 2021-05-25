n = int(input())
arr = [0]*10
n = str(n)
for i in n:
    arr[int(i)] += 1

MAX = max(arr)
ans = []


for i in range(10):
    if arr[i] == MAX and i not in [6, 9]:
        ans.append(arr[i])
        break
    elif arr[i] == MAX and i in [6, 9]:
        if (arr[6] + arr[9]) % 2 == 0:
            ans.append((arr[6] + arr[9]) // 2)
        else:
            ans.append(((arr[6] + arr[9]) // 2) + 1)

print(max(ans))
