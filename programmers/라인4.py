# arr = [6, 2, 2, 6]
# brr = [4, 4, 4, 4]
arr = [3, 7, 2, 4]
brr = [4, 5, 5, 2]

def solution(arr, brr):
    tmp = []
    n = len(arr)
    for i in range(n):
        tmp.append(arr[i] - brr[i])
    print(tmp)
    ans = 0
    for i in range(n-1):
        if tmp.count(0) == n:
            break
        d = 0 - tmp[i]
        if d == 0:
            continue
        ans += 1


        tmp[i] += d
        tmp[i + 1] -= d

    return ans

print(solution(arr, brr))