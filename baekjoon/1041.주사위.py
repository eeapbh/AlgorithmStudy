n = int(input())
arr = list(map(int, input().split()))
ans = 0
min_list = []
if n == 1:
    arr.sort()
    for i in range(5):
        ans += arr[i]
else:
    min_list.append(min(arr[0], arr[5]))
    min_list.append(min(arr[1], arr[4]))
    min_list.append(min(arr[2], arr[3]))
    min_list.sort()
    m1 = min_list[0]
    m2 = min_list[0] + min_list[1]
    m3 = min_list[0] + min_list[1] + min_list[2]
    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    ans += n1 * m1
    ans += n2 * m2
    ans += n3 * m3
print(ans)